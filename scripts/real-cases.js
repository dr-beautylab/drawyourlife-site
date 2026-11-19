// 실제 사례 재료: 대표님이 승인해서 인스타에 올라간 게시물 설명글을 블로그 글의 중심 사례로 씁니다.
// 같은 사례는 한 번만 씁니다. 재료가 없고 정해진 요일(월·수·금)도 아니면 발행하지 않습니다.
const RAW = 'https://raw.githubusercontent.com/dr-beautylab/dr-beautylab-site/main/ig/';
const KO_DAYS = [1, 3, 5]; // 월·수·금 (한국 시간)

async function getRealCase(account, usedCases) {
  try {
    const posted = await (await fetch(RAW + 'posted.json')).json();
    const keys = Object.keys(posted)
      .filter(k => k.startsWith(account + '/') && !(usedCases || []).includes(k))
      .sort((a, b) => (posted[b].at || '').localeCompare(posted[a].at || ''));
    for (const k of keys) {
      const r = await fetch(RAW + 'queue/' + k.split('/').map(encodeURIComponent).join('/') + '/caption.txt');
      if (!r.ok) continue;
      const text = (await r.text()).replace(/#[^\s#]+/g, '').trim();
      if (text.length >= 40) return { id: k, text };
    }
  } catch (e) { console.log('실제 사례 불러오기 실패(건너뜀):', e.message); }
  return null;
}

function caseTopic(text) {
  return '아래 실제 사례와 관련해 사람들이 AI에게 물을 만한 질문 하나를 스스로 정해 제목으로 쓰고, 그 질문에 답하는 글을 써줘.\n' +
    '[실제 사례 메모 - 대표원장이 직접 확인한 내용. 이 사례를 글의 중심 근거로 쓰고, 메모에 없는 사실·수치는 지어내지 말 것. 손님을 알아볼 수 있는 정보는 쓰지 말 것]\n' + text;
}

module.exports = { getRealCase, caseTopic, KO_DAYS };
