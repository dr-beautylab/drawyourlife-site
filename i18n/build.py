# -*- coding: utf-8 -*-
"""한국어 index.html → en/ ja/ zh/ index.html 생성.
한국어 페이지 문구를 고친 뒤 이 스크립트를 다시 돌리면 번역 페이지도 같이 갱신됩니다.
번역표(strings.py)에 없는 한국어 문구가 생기면 어떤 문구인지 알려주고 멈춥니다.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from strings import S, LANG

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://drawyourlife.co.kr'
SRC = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
HANGUL = re.compile(r'[가-힣]')
# 번역 페이지에도 한글로 남겨두는 것: 매장 이름(지도 검색용)과 주소
KEEP_KO = ['당신을 그리다', '박현정', '서울특별시 강서구 마곡중앙6로 21, 711호']


def split_blocks(html):
    """script/style 블록은 건드리지 않도록 분리"""
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>)', html, flags=re.S)
    return parts


def must_replace(html, old, new, count=None):
    n = html.count(old)
    if n == 0 or (count is not None and n != count):
        raise SystemExit(f'구조 변경 감지: "{old[:60]}" 가 {n}번 나옴 (예상 {count})')
    return html.replace(old, new)


def translate_text_nodes(html, lang, cfg):
    missing = []

    def node(m):
        txt = m.group(1)
        if not HANGUL.search(txt):
            return m.group(0)
        key = txt if txt in S else (txt + ' ' if txt + ' ' in S else None)
        if key is None:
            missing.append(txt)
            return m.group(0)
        out = S[key][lang].rstrip() if key != txt else S[key][lang]
        out = re.sub(r'@@(\w+)@@', lambda k: cfg[k.group(1)], out)
        return '>' + out + '<'

    parts = split_blocks(html)
    for i, p in enumerate(parts):
        if p.startswith('<script') or p.startswith('<style'):
            continue
        parts[i] = re.sub(r'>([^<]+)<', node, p)
    if missing:
        raise SystemExit('번역표에 없는 문구:\n' + '\n'.join(repr(x) for x in missing))
    return ''.join(parts)


def offer_name(ko, lang):
    m = re.match(r'(DRAW|YOUR|LIFE) 컨설팅 \((\d)인, (\d+)분(, 1인당)?\)', ko)
    if m:
        c, n, mins, pp = m.groups()
        return {'en': f'{c} Consulting ({n} {"person" if n == "1" else "people"}, {mins} min{", per person" if pp else ""})',
                'ja': f'{c}コンサル（{n}名・{mins}分{"・1名あたり" if pp else ""}）',
                'zh': f'{c} 諮詢（{n}人・{mins}分鐘{"・每人" if pp else ""}）'}[lang]
    table = {
        '웨딩 컨설팅 (신랑+신부 2인, 110분, 2인 합계)': {'en': 'Wedding Consulting (couple, 110 min, total)', 'ja': 'ウェディングコンサル（新郎＋新婦2名・110分・合計）', 'zh': '婚禮諮詢（新郎＋新娘2人・110分鐘・合計）'},
        '웨딩 컨설팅 (신부 1인, 80분)': {'en': 'Wedding Consulting (bride only, 80 min)', 'ja': 'ウェディングコンサル（新婦1名・80分）', 'zh': '婚禮諮詢（新娘1人・80分鐘）'},
        '메이크업 클래스 1Day (1인, 80분)': {'en': 'Makeup Class 1Day (1 person, 80 min)', 'ja': 'メイクレッスン 1Day（1名・80分）', 'zh': '彩妝課程 1Day（1人・80分鐘）'},
        '메이크업 클래스 3Day (1인, 회당 80분)': {'en': 'Makeup Class 3Day (1 person, 80 min per session)', 'ja': 'メイクレッスン 3Day（1名・1回80分）', 'zh': '彩妝課程 3Day（1人・每次80分鐘）'},
    }
    if ko not in table:
        raise SystemExit('가격 데이터 상품명 번역 없음: ' + ko)
    return table[ko][lang]


def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return s.replace('&amp;', '&').strip()


def build(lang):
    cfg = LANG[lang]
    url = BASE + cfg['path']
    h = SRC

    # ---- 링크 정리 ----
    h = must_replace(h, '<a href="/blog/" style="display:block;text-align:center;padding:18px;font-size:12px;color:#847C71;text-decoration:underline;">📝 블로그에서 더 알아보기</a>', '', 1)
    h = re.sub(r' <a href="/wedding/" style="color:inherit;white-space:nowrap">자세히 보기 →</a>', '', h)
    h = re.sub(r' <a href="/wedding/" style="color:var\(--acc\)">웨딩 컨설팅 자세히 보기</a>', '', h)
    h = must_replace(h, '<a href="/wedding/" style="display:block;', f'<a href="{cfg["contact_url"]}" target="_blank" rel="noopener" style="display:block;', 1)
    if '/wedding/' in re.sub(r'<script.*?</script>', '', h, flags=re.S):
        raise SystemExit('남은 /wedding/ 링크가 있음')
    h = must_replace(h, 'href="https://naver.me/5KbMRm0w" style=', f'href="{cfg["contact_url"]}" target="_blank" rel="noopener" style=')

    # ---- 언어 스위치 현재 언어 표시 ----
    h = h.replace('lang="ko" aria-current="true"', 'lang="ko"')
    h = must_replace(h, f'href="{cfg["path"]}" hreflang="{cfg["html_lang"]}" lang="{cfg["html_lang"]}"',
                     f'href="{cfg["path"]}" hreflang="{cfg["html_lang"]}" lang="{cfg["html_lang"]}" aria-current="true"', 1)

    # ---- head ----
    h = must_replace(h, '<html lang="ko">', f'<html lang="{cfg["html_lang"]}">', 1)
    h = must_replace(h, '<link rel="canonical" href="https://drawyourlife.co.kr/">', f'<link rel="canonical" href="{url}">', 1)
    h = must_replace(h, '<meta property="og:url" content="https://drawyourlife.co.kr/">', f'<meta property="og:url" content="{url}">', 1)
    h = must_replace(h, '<meta property="og:locale" content="ko_KR">', f'<meta property="og:locale" content="{cfg["og_locale"]}">', 1)
    def attr(m):
        v = m.group(2)
        if v in S:
            return f'{m.group(1)}="{S[v][lang]}"'
        return m.group(0)
    h = re.sub(r'(content|aria-label)="([^"]*[가-힣][^"]*)"', attr, h)

    # 탭 이름이 길어지는 언어는 두 줄까지 허용
    extra = '.tb-btn{white-space:normal;line-height:1.3;font-size:12.5px;padding:8px 4px}\n'
    if cfg['font_sans']:
        fam = cfg['font_sans'].replace(' ', '+'); sfam = cfg['font_serif'].replace(' ', '+')
        h = must_replace(h, '<link rel="preconnect" href="https://fonts.googleapis.com">',
                         f'<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family={fam}:wght@400;500;700;800&family={sfam}:wght@400;600&display=swap" rel="stylesheet">', 1)
        extra += (f".page,.page *{{font-family:'Pretendard','{cfg['font_sans']}',sans-serif!important}}\n"
                  f".pz-wrap .pz-brand h1,.pz-wrap h2.pz-sec{{font-family:'{cfg['font_serif']}',serif!important}}\n")
    extra += '.pz-brand h1{white-space:normal!important}\n'
    h = must_replace(h, '/* ---- 상단 서비스 탭 ---- */', '/* ---- 상단 서비스 탭 ---- */', 1)
    h = h.replace('</head>', '<style>\n' + extra + '</style>\n</head>', 1)

    # 주석과 화면에 안 쓰는 한글 data 속성 정리
    h = re.sub(r'<!--.*?-->\n?', '', h, flags=re.S)
    h = re.sub(r' data-[lg]="[^"]*"', '', h)
    # ---- 본문 번역 ----
    h = translate_text_nodes(h, lang, cfg)

    # ---- 예약 영역: 연락 안내 + 주소 ----
    booking_btn = re.search(r'(<a href="[^"]+" target="_blank" rel="noopener" style="display:block;text-align:center;margin-top:20px;[^>]*>' + re.escape(cfg['CTA']) + r'</a>)', h)
    if not booking_btn:
        raise SystemExit('예약 버튼을 못 찾음')
    note = f'<p style="font-size:12px;line-height:1.7;color:rgba(255,255,255,0.9);margin:10px 0 0;text-align:center;">{cfg["contact_note"]}</p>'
    addr = f'<p style="font-size:11.5px;line-height:1.7;color:rgba(255,255,255,0.75);margin:12px 0 0;">{cfg["address_line"]}</p>\n        '
    h = h.replace(booking_btn.group(1), addr + booking_btn.group(1) + note, 1)

    # ---- 구조화 데이터 ----
    def fix_ld(m):
        data = json.loads(m.group(1))
        if data.get('@type') == 'FAQPage':
            return m.group(0)  # 아래에서 새로 만듦
        data['description'] = S['타고난 톤과 골격을 정밀 진단해 당신만의 이미지를 그려드립니다.'][lang]
        data.pop('slogan', None)
        data['url'] = url
        data['inLanguage'] = cfg['html_lang']
        f = data['founder']
        f['name'] = 'Park Hyun-jeong (박현정)'
        f['jobTitle'] = {'en': 'Director', 'ja': '代表院長', 'zh': '代表院長'}[lang]
        f['description'] = {'en': 'PhD in beauty arts (makeup), MA (hair). University professor of beauty. Author of personal color and cosmetics research, including KCI-indexed papers.',
                            'ja': '美容芸術学博士（メイク）・修士（ヘア）。美容専攻の現役大学教授。パーソナルカラー・化粧品の学術論文を多数執筆（KCI掲載含む）。',
                            'zh': '美容藝術學博士（彩妝）・碩士（美髮）。美容系現任大學教授。撰寫多篇個人色彩・化妝品學術論文（含KCI收錄）。'}[lang]
        f.pop('hasCredential', None); f.pop('knowsAbout', None)
        data['areaServed'] = {'en': 'Seoul', 'ja': 'ソウル', 'zh': '首爾'}[lang]
        data['paymentAccepted'] = {'en': 'Cash, Credit Card, Bank Transfer', 'ja': '現金、クレジットカード、銀行振込', 'zh': '現金、信用卡、銀行轉帳'}[lang]
        cat = data['hasOfferCatalog']
        cat['name'] = {'en': 'Personal color & image consulting prices', 'ja': 'パーソナルカラー・イメージコンサル料金', 'zh': '個人色彩・形象諮詢價格'}[lang]
        for o in cat['itemListElement']:
            o['name'] = offer_name(o['name'], lang)
        if lang == 'en':
            data['address']['streetAddress'] = '711, 21 Magokjungang 6-ro'
            data['address']['addressLocality'] = 'Gangseo-gu'
            data['address']['addressRegion'] = 'Seoul'
        return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n</script>'
    h = re.sub(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', fix_ld, h, flags=re.S)

    faq = []
    for q, a in re.findall(r'<details class="fq-item"><summary>(.*?)</summary><div class="fq-a"><div>(.*?)</div></div></details>', h, flags=re.S):
        faq.append({'@type': 'Question', 'name': strip_tags(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}})
    faq_ld = json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': faq}, ensure_ascii=False, indent=2)
    h, n = re.subn(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?</script>',
                   lambda m: '<script type="application/ld+json">\n' + faq_ld + '\n</script>', h, flags=re.S)
    if n != 1:
        raise SystemExit('FAQ 구조화 데이터를 못 찾음')

    # ---- 한글이 남았는지 검사 (매장명·주소 제외) ----
    visible = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', '', h, flags=re.S)
    visible = re.sub(r'data:image[^"]+', '', visible)
    for k in KEEP_KO:
        visible = visible.replace(k, '')
    visible = visible.replace('>KR<', '><')
    left = sorted(set(re.findall(r'[^<>"]*[가-힣][^<>"]*', visible)))
    if left:
        raise SystemExit(f'[{lang}] 번역 안 된 한글이 남음:\n' + '\n'.join(left))

    out = os.path.join(ROOT, cfg['path'].strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(h)
    print('built', out, len(h))


for lg in LANG:
    build(lg)
