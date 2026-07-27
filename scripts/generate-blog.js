// 자동 블로그 발행 스크립트
// 실행: node scripts/generate-blog.js
// 필요 환경변수: ANTHROPIC_API_KEY (GitHub Secrets에서 자동 주입됨)

const fs = require('fs');
const path = require('path');

const ROOT = process.cwd();
const CONFIG_PATH = path.join(ROOT, 'blog', 'config.json');
const USED_PATH = path.join(ROOT, 'blog', 'used-topics.json');
const POSTS_DIR = path.join(ROOT, 'blog', 'posts');
const INDEX_PATH = path.join(ROOT, 'blog', 'index.html');
const SITEMAP_PATH = path.join(ROOT, 'sitemap.xml');
const ROBOTS_PATH = path.join(ROOT, 'robots.txt');

function readJSON(p, fallback) {
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch (e) { return fallback; }
}

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^\w가-힣\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .slice(0, 60);
}

async function callClaude(config, topic) {
  const systemPrompt = `당신은 "${config.siteName}"의 SEO/GEO 콘텐츠 작가입니다.
오로지 GEO(Generative Engine Optimization), SEO 관점에서만 작성해주세요.
이 글은 사람이 감성적으로 즐기며 읽는 글이 아니라, 검색엔진과 AI(챗GPT, 퍼플렉시티, 제미나이 등)가 이 업체를 정확하게 파싱하고 요약·인용해서 소개할 수 있도록 만드는 "정보성 콘텐츠"입니다.
- 사실 기반, 구체적인 정보 위주로 작성 (모호한 미사여구 최소화)
- 업체명, 서비스명, 지역 키워드를 자연스럽게 반복 언급
- 소제목(h2, h3)으로 구조화해서 AI가 파싱하기 쉽게 작성
- 1200~1800자 분량
- 과장 광고 문구 지양, 정확하고 신뢰도 있는 톤
- "소비자가 읽는다"가 아니라 "AI가 읽어간다"는 전제로, 힘 빼고 정확하게 정보를 나열

업체 정보:
${config.businessInfo}
`;

  const userPrompt = `다음 주제로 글을 작성해줘: "${topic}"

아래 JSON 형식으로만 응답해줘 (다른 설명 없이 JSON만):
{
  "title": "글 제목",
  "metaDescription": "검색결과에 노출될 150자 이내 요약",
  "bodyHtml": "본문 HTML (h2, h3, p, ul/li 태그만 사용, style 속성 없이)"
}`;

  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: 'claude-sonnet-5',
      max_tokens: 3000,
      system: systemPrompt,
      messages: [{ role: 'user', content: userPrompt }]
    })
  });

  if (!res.ok) {
    const errText = await res.text();
    throw new Error(`Claude API 오류 (${res.status}): ${errText}`);
  }

  const data = await res.json();
  const text = data.content.map(b => b.text || '').join('');
  const cleaned = text.replace(/```json|```/g, '').trim();
  return JSON.parse(cleaned);
}

// HTML 속성에 넣을 문자열을 안전하게 이스케이프합니다.
// 생성된 제목/요약에 따옴표가 섞이면 메타 태그가 통째로 깨집니다.
function esc(s) {
  return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;')
                  .replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// AI가 만든 제목이 이미 업체명으로 끝나면 뒤에 또 붙이지 않습니다.
function pageTitle(config, title) {
  return title.includes(config.siteName) ? title : `${title} | ${config.siteName}`;
}

// 본문의 '자주 묻는 질문' 섹션을 FAQPage 구조화 데이터로 바꿉니다.
// AI 검색은 질문-답변 쌍을 통째로 인용하기 때문에, 본문에만 두면 절반만 쓰는 셈입니다.
function extractFaq(bodyHtml) {
  const i = bodyHtml.search(/<h2[^>]*>[^<]*자주\s*묻는\s*질문[^<]*<\/h2>/);
  if (i < 0) return null;
  const tail = bodyHtml.slice(i);
  const qa = [];
  const re = /<h3[^>]*>([\s\S]*?)<\/h3>\s*((?:<(?:p|ul|ol)[^>]*>[\s\S]*?<\/(?:p|ul|ol)>\s*)+)/g;
  let m;
  while ((m = re.exec(tail))) {
    const q = m[1].replace(/<[^>]+>/g, '').trim();
    const a = m[2].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    if (q && a) qa.push({ '@type': 'Question', name: q,
      acceptedAnswer: { '@type': 'Answer', text: a } });
  }
  if (!qa.length) return null;
  return { '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: qa };
}

function buildPostHTML(config, post, dateStr, others) {
  const t = config.theme;
  const base = (config.siteUrl || '').replace(/\/$/, '');
  const url = `${base}/blog/posts/${encodeURIComponent(post.slug)}.html`;
  const img = `${base}/og.jpg`;
  const title = pageTitle(config, post.title);
  const faq = extractFaq(post.bodyHtml);

  const article = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    mainEntityOfPage: { '@type': 'WebPage', '@id': url },
    headline: post.title.slice(0, 110),
    description: post.metaDescription,
    image: img,
    inLanguage: 'ko-KR',
    datePublished: dateStr,
    dateModified: dateStr,
    author: { '@type': 'Organization', name: config.siteName, url: base + '/' },
    publisher: { '@type': 'Organization', name: config.siteName,
                 logo: { '@type': 'ImageObject', url: img } }
  };

  // 다른 글로 이어지는 링크. 크롤러가 글을 타고 돌 수 있게 하고,
  // 독자에게도 다음 읽을거리를 줍니다.
  const related = (others || []).slice(0, 3).map(p =>
    `<li><a href="${encodeURIComponent(p.slug)}.html">${esc(p.title)}</a></li>`).join('');

  return `<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${esc(title)}</title>
<meta name="description" content="${esc(post.metaDescription)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="${url}">
<meta property="og:type" content="article">
<meta property="og:title" content="${esc(post.title)}">
<meta property="og:description" content="${esc(post.metaDescription)}">
<meta property="og:url" content="${url}">
<meta property="og:image" content="${img}">
<meta property="og:site_name" content="${esc(config.siteName)}">
<meta property="og:locale" content="ko_KR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(post.title)}">
<meta name="twitter:description" content="${esc(post.metaDescription)}">
<meta name="twitter:image" content="${img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Noto+Serif+KR:wght@400;600;700&family=Song+Myung&family=Gowun+Batang:wght@400;700&family=Gothic+A1:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
<script type="application/ld+json">
${JSON.stringify(article, null, 2)}
</script>${faq ? `
<script type="application/ld+json">
${JSON.stringify(faq, null, 2)}
</script>` : ''}
<style>
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#ddd;display:flex;justify-content:center;font-family:${t.fBody};}
.page{width:100%;max-width:600px;background:${t.bg};color:${t.ink};min-height:100vh;word-break:keep-all;padding:32px 24px 60px;}
.back{display:inline-block;font-size:13px;color:${t.acc};margin-bottom:20px;text-decoration:none;}
h1{font-family:${t.fDisplay};font-size:24px;line-height:1.4;margin-bottom:10px;}
.date{font-size:12px;color:${t.inkSoft};margin-bottom:24px;}
h2{font-family:${t.fDisplay};font-size:19px;margin:28px 0 10px;}
h3{font-size:16px;margin:20px 0 8px;}
p{font-size:14.5px;line-height:1.8;margin-bottom:14px;color:${t.ink};}
ul{margin:0 0 14px 20px;}
li{font-size:14.5px;line-height:1.8;margin-bottom:6px;}
.cta{margin:36px 0 0;padding:22px 20px;background:${t.acc};border-radius:14px;color:#fff;}
.cta p{color:rgba(255,255,255,.85);font-size:13px;margin-bottom:14px;}
.cta strong{display:block;font-size:16px;margin-bottom:8px;color:#fff;}
.cta a{display:block;text-align:center;background:#fff;color:${t.accDark};font-weight:800;
       padding:13px;border-radius:100px;font-size:14.5px;text-decoration:none;}
.more{margin-top:30px;padding-top:18px;border-top:1px solid ${t.line};}
.more b{font-size:13px;color:${t.inkSoft};display:block;margin-bottom:8px;}
.more li{font-size:13.5px;margin-bottom:6px;}
.more a{color:${t.acc};text-decoration:none;}
.home{display:block;text-align:center;margin-top:24px;font-size:13px;color:${t.inkSoft};text-decoration:underline;}
</style></head><body><div class="page">
<a class="back" href="../index.html">← 블로그 목록으로</a>
<h1>${esc(post.title)}</h1>
<div class="date">${dateStr} · ${esc(config.siteName)}</div>
${post.bodyHtml}
<div class="cta">
  <strong>${esc(config.siteName)}</strong>
  <p>${esc(config.ctaText || '상담과 예약은 네이버 예약으로 받고 있습니다.')}</p>
  <a href="${config.bookingUrl || '#'}" target="_blank" rel="noopener">네이버 예약하기</a>
</div>${related ? `
<div class="more"><b>함께 보면 좋은 글</b><ul>${related}</ul></div>` : ''}
<a class="home" href="../../index.html">${esc(config.siteName)} 홈으로</a>
</div></body></html>`;
}

function updateBlogIndex(config, posts) {
  const t = config.theme;
  const base = (config.siteUrl || '').replace(/\/$/, '');
  const desc = `${config.siteName}이(가) 직접 정리한 정보 글 모음입니다.`;
  const items = posts.map(p => `
    <a href="posts/${encodeURIComponent(p.slug)}.html" style="display:block;padding:16px 0;border-bottom:1px solid ${t.line};text-decoration:none;color:${t.ink};">
      <div style="font-size:15px;font-weight:700;margin-bottom:4px;">${esc(p.title)}</div>
      <div style="font-size:12px;color:${t.inkSoft};">${p.date}</div>
    </a>`).reverse().join('');

  const html = `<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>블로그 | ${esc(config.siteName)}</title>
<meta name="description" content="${esc(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="${base}/blog/index.html">
<meta property="og:type" content="website">
<meta property="og:title" content="블로그 | ${esc(config.siteName)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:url" content="${base}/blog/index.html">
<meta property="og:image" content="${base}/og.jpg">
<meta property="og:site_name" content="${esc(config.siteName)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Noto+Serif+KR:wght@400;600;700&family=Song+Myung&family=Gowun+Batang:wght@400;700&family=Gothic+A1:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#ddd;display:flex;justify-content:center;font-family:${t.fBody};}
.page{width:100%;max-width:600px;background:${t.bg};color:${t.ink};min-height:100vh;padding:32px 24px 60px;}
.back{display:inline-block;font-size:13px;color:${t.acc};margin-bottom:20px;text-decoration:none;}
h1{font-family:${t.fDisplay};font-size:22px;margin-bottom:20px;}
</style></head><body><div class="page">
<a class="back" href="../index.html">← 홈으로</a>
<h1>${esc(config.siteName)} 블로그</h1>
${items || '<p style="color:' + t.inkSoft + ';font-size:13px;">아직 글이 없어요.</p>'}
</div></body></html>`;
  fs.writeFileSync(INDEX_PATH, html, 'utf8');
}

function updateSitemap(config, posts) {
  if (!config.siteUrl) {
    console.warn('config.json에 siteUrl이 없어서 sitemap.xml을 건너뜁니다.');
    return;
  }
  const base = config.siteUrl.replace(/\/$/, '');
  // 사이트맵 규격상 URL 은 퍼센트 인코딩해야 합니다.
  // 한글을 그대로 두면 네이버 서치어드바이저가 사이트맵을 거부합니다.
  // lastmod 를 넣으면 검색엔진이 새 글만 골라 다시 읽어갑니다.
  const today = new Date().toISOString().slice(0, 10);
  const urls = [
    { loc: `${base}/`, mod: today },
    { loc: `${base}/blog/index.html`, mod: today },
    ...posts.map(p => ({
      loc: `${base}/blog/posts/${encodeURIComponent(p.slug)}.html`,
      mod: p.date || today
    }))
  ];
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url><loc>${u.loc}</loc><lastmod>${u.mod}</lastmod></url>`).join('\n')}
</urlset>
`;
  fs.writeFileSync(SITEMAP_PATH, xml, 'utf8');

  if (!fs.existsSync(ROBOTS_PATH)) {
    fs.writeFileSync(ROBOTS_PATH, `User-agent: *\nAllow: /\nSitemap: ${base}/sitemap.xml\n`, 'utf8');
  }
}

async function main() {
  const config = readJSON(CONFIG_PATH, null);
  if (!config) {
    console.error('blog/config.json 파일이 없습니다. 먼저 config.json을 만들어주세요.');
    process.exit(1);
  }

  const used = readJSON(USED_PATH, { usedTopics: [], posts: [] });
  let remaining = config.topics.filter(t => !used.usedTopics.includes(t));
  if (remaining.length === 0) {
    used.usedTopics = [];
    remaining = config.topics.slice();
  }
  const topic = remaining[0];

  console.log('선택된 주제:', topic);

  const post = await callClaude(config, topic);
  const slug = slugify(post.title) || slugify(topic) || ('post-' + Date.now());
  const dateStr = new Date().toISOString().slice(0, 10);

  if (!fs.existsSync(POSTS_DIR)) fs.mkdirSync(POSTS_DIR, { recursive: true });
  const postHtml = buildPostHTML(config, post, dateStr, (used.posts||[]).slice(-3));
  fs.writeFileSync(path.join(POSTS_DIR, slug + '.html'), postHtml, 'utf8');

  used.usedTopics.push(topic);
  used.posts.push({ slug, title: post.title, date: dateStr });
  fs.writeFileSync(USED_PATH, JSON.stringify(used, null, 2), 'utf8');

  updateBlogIndex(config, used.posts);
  updateSitemap(config, used.posts);

  console.log('발행 완료:', post.title);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
