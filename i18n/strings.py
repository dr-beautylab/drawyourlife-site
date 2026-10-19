# -*- coding: utf-8 -*-
# 홈페이지(index.html) 번역 문구표
# 키 = 한국어 원문 텍스트(태그 사이 글자 그대로), 값 = 언어별 번역
# 한국어 index.html 문구를 바꾸면 여기 키도 같이 바꿔야 번역 페이지에 반영됩니다.
# 빌드: python3 i18n/build.py  → en/ ja/ zh/ index.html 생성

S = {}
def t(ko, en, ja, zh):
    S[ko] = {'en': en, 'ja': ja, 'zh': zh}

# ---------- 기본 / 히어로 ----------
t('당신을 그리다 | 퍼스널 이미지 컨설팅',
  'Draw Your Life (당신을 그리다) | Personal Color & Image Consulting in Seoul',
  'Draw Your Life（당신을 그리다）| ソウルのパーソナルカラー・イメージコンサルティング',
  'Draw Your Life（당신을 그리다）| 首爾個人色彩・形象諮詢')
t('타고난 톤과 골격을 정밀 진단해 당신만의 이미지를 그려드립니다.',
  'Personal color and bone-structure analysis by a Korean beauty professor, near Gimpo Airport in Seoul.',
  '美容学博士・美容専攻の大学教授が直接行うパーソナルカラー＆骨格診断。ソウル・金浦空港近く。',
  '由美容學博士・美容系大學教授親自進行的個人色彩與骨架診斷。首爾金浦機場附近。')
t('당신을 그리다', 'Draw Your Life', 'Draw Your Life', 'Draw Your Life')
t('서비스 선택', 'Choose a service', 'サービスを選ぶ', '選擇服務')
t('미용학 박사·뷰티전공 대학교수 직접 진단',
  'Analyzed in person by a PhD and university beauty professor',
  '美容学博士・美容専攻の大学教授が直接診断',
  '美容學博士・美容系大學教授親自診斷')
t('나만의 아름다움을 완성하는 토탈 퍼스널 이미지, ',
  'Total personal image consulting to bring out your own beauty — ',
  'あなただけの美しさを完成させるトータル・パーソナルイメージ、',
  '成就專屬於你的美，全方位個人形象諮詢 ')
t('공장형 컨설팅 NO,\n오롯이 당신만을 위한 프라이빗 컨설팅',
  'No assembly-line sessions.\nA private consultation, just for you.',
  '流れ作業のコンサルはしません。\nあなただけのためのプライベートコンサルティング。',
  '拒絕流水線式諮詢，\n只為你一人的私人諮詢。')
t('누적 진단', 'Analyses to date', '累計診断', '累計診斷')
t('20,000건+', '20,000+', '20,000件+', '20,000件+')
t('국내 1세대', 'Pioneer in Korea', '韓国パーソナルカラー第1世代', '韓國第一代')
t('2016년부터', 'Since 2016', '2016年から', '2016年起')
t('전국에서 찾아오는 업체', 'Clients from', '韓国全土からご来店', '客人遍布全韓')
t('17개 시·도', 'All 17 regions', '全17地域', '17個市・道')
t('네이버 예약하기', '@@CTA@@', '@@CTA@@', '@@CTA@@')
t('네이버 예약하기 →', '@@CTA@@ →', '@@CTA@@ →', '@@CTA@@ →')

# ---------- 탭 ----------
t('이미지 컨설팅', 'Image Consulting', 'イメージコンサル', '形象諮詢')
t('웨딩 컨설팅', 'Wedding Consulting', 'ウェディング', '婚禮諮詢')
t('메이크업 컨설팅', 'Makeup Class', 'メイクレッスン', '彩妝課程')

# ---------- 대표원장 ----------
t('대표원장 박현정', 'Director Park Hyun-jeong', '代表院長 パク・ヒョンジョン', '代表院長 Park Hyun-jeong（박현정）')
t('퍼스널컬러 KCI 등재 논문', 'KCI-indexed personal color papers', 'パーソナルカラーのKCI掲載論文', 'KCI收錄色彩論文')
t('뷰티전공 대학교수', 'University beauty professor', '美容専攻 大学教授', '美容系大學教授')
t('메이크업 박사 · 헤어 석사', 'PhD in Makeup · MA in Hair', 'メイク博士・ヘア修士', '彩妝博士・美髮碩士')
t('미용경력 15년차', '15 years in beauty', '美容歴15年', '美容資歷15年')
t("· 이미지 컨설팅 전문 '당신을 그리다' 대표\n· 퍼스널컬러 / 화장품 관련 학술 논문 다수 집필 (KCI 등재 포함)\n· 대한민국 국회 최우수지도자 표창 4회 수상\n· KRYOLAN Global Make Up Artist\n· 퍼스널컬러 컨설턴트 강사 자격증 보유\n· PIVOT POINT Diploma 4종 보유(헤어)\n-Salonability Long Hair / HAIR DESIGN\n-Perm Design / Salonability Cut&Color\n· 2016 OMC KOREA 무궁화컵 스파니엘 커트 은상\n· 국제 뷰티 심사위원 1급 자격\n· 미용사(종합) 면허증 보유",
  "· Founder of Draw Your Life, an image consulting studio\n· Author of numerous academic papers on personal color and cosmetics (incl. KCI-indexed)\n· 4-time recipient of the National Assembly of Korea Award for Outstanding Instructor\n· KRYOLAN Global Make Up Artist\n· Certified personal color consultant instructor\n· 4 PIVOT POINT Diplomas (hair)\n-Salonability Long Hair / HAIR DESIGN\n-Perm Design / Salonability Cut&Color\n· 2016 OMC KOREA Mugunghwa Cup, Spaniel Cut, Silver Award\n· International Beauty Judge, Level 1\n· Licensed cosmetologist (Korea, general license)",
  "· イメージコンサルティング専門「Draw Your Life」代表\n· パーソナルカラー・化粧品に関する学術論文を多数執筆（KCI掲載含む）\n· 大韓民国国会 最優秀指導者表彰 4回受賞\n· KRYOLAN Global Make Up Artist\n· パーソナルカラーコンサルタント講師資格\n· PIVOT POINT Diploma 4種（ヘア）\n-Salonability Long Hair / HAIR DESIGN\n-Perm Design / Salonability Cut&Color\n· 2016 OMC KOREA 無窮花カップ スパニエルカット 銀賞\n· 国際ビューティー審査員 1級\n· 美容師（総合）免許",
  "· 形象諮詢工作室「Draw Your Life」代表\n· 撰寫多篇個人色彩・化妝品相關學術論文（含KCI收錄）\n· 榮獲大韓民國國會最優秀指導者表揚 4次\n· KRYOLAN Global Make Up Artist\n· 個人色彩顧問講師證照\n· PIVOT POINT Diploma 4項（美髮）\n-Salonability Long Hair / HAIR DESIGN\n-Perm Design / Salonability Cut&Color\n· 2016 OMC KOREA 無窮花盃 Spaniel Cut 銀獎\n· 國際美容評審 1級證照\n· 美容師（綜合）執照")

# ---------- 후기 ----------
t('고객 리얼 후기', 'Real reviews', 'お客様の声', '顧客真實評價')
t('네이버 리뷰 더보기 →', 'More reviews on Naver →', 'NAVERで続きを見る →', '在 Naver 看更多 →')
t('네이버 예약 리뷰', 'Naver booking review (translated)', 'NAVER予約レビュー（翻訳）', 'Naver 預約評價（翻譯）')
t('친구랑 퍼스널 진단＋원데이 메이크업 클래스 받으러 왔어요.',
  'Came with a friend for personal color analysis + a one-day makeup class.',
  '友達とパーソナルカラー診断＋ワンデーメイクレッスンを受けに来ました。',
  '和朋友一起來做個人色彩診斷＋一日彩妝課。')
t('\n        꼼꼼하게 설명해주시고, 제품도 하나하나 추천해 주셔서 오길 정말 잘 했다는 생각이 들었어요!',
  "\n        She explained everything carefully and recommended products one by one — I'm so glad I came!",
  '\n        丁寧に説明してくださって、コスメも一つひとつおすすめしてもらえて、本当に来てよかったです！',
  '\n        老師解說得很仔細，還一個一個推薦產品，真的很慶幸有來！')
t('\n        앞으로 옷 살 때랑 메이크업 할 때 고민 안 해도 될 것 같아 넘 좋습니다ㅎㅎ 감사합니다!',
  "\n        No more agonizing when I shop for clothes or do my makeup. Thank you!",
  '\n        これからは服選びもメイクも迷わなくて済みそうで嬉しいです。ありがとうございました！',
  '\n        以後買衣服、化妝都不用再煩惱了，太好了，謝謝！')
t('저번에 퍼스널 컬러 하면서 메이크업 수업이랑 같이 병행했었는데 너무 만족스러워서 이번에는 동생이랑 같이 메이크업 클래스 들었습니다!',
  'Last time I did personal color analysis along with a makeup lesson and loved it, so this time I took the makeup class with my sister!',
  '前回パーソナルカラーとメイクレッスンを一緒に受けてとても満足だったので、今回は妹とメイクレッスンを受けました！',
  '上次做個人色彩時一起上了彩妝課，非常滿意，所以這次和妹妹一起來上彩妝課！')
t('\n        오늘도 제가 원하는 스타일과 어떻게 하면 좋을지 꼼꼼하게 봐주셔서 재밌게 수업듣는거 같습니당!',
  '\n        Again she looked closely at the style I wanted and how to get there — the class was so much fun!',
  '\n        今日も私の希望のスタイルと、どうすれば良いかを丁寧に見てくださって、楽しくレッスンを受けられました！',
  '\n        今天也仔細看了我想要的風格和該怎麼畫，上課很開心！')
t('\n        오늘 배운거 꾸준히 연습해서 다음번에는 다른 메이크업 배우러 오겠습니다~~!!',
  "\n        I'll keep practicing what I learned and come back to learn another look!",
  '\n        今日習ったことをコツコツ練習して、次は別のメイクを習いに来ます！',
  '\n        會好好練習今天學的，下次再來學別的妝！')
t('30살되기전에 꼭 받아보고 싶었는데 만족도 최상이에요',
  "I wanted to do this before turning 30, and I couldn't be happier.",
  '30歳になる前にぜひ受けてみたかったのですが、大満足です！',
  '一直很想在30歲之前做一次，滿意度爆表！')
t('\n        화장법도 자세하게 하나하나 다 알려주시고 제 색깔을 찾아서 속시원했습니더ㅜㅠ 옷스타일부터 악세사리까지 하나하나 집어주셔서 좋았습니다! 궁금한거 다 물어봐도 친절하게 알려주시고 분위기도 좋아서 편안하게',
  '\n        She taught me makeup step by step, and finally finding my colors was such a relief. She went through everything with me, from clothing styles to accessories! She kindly answered every question, and the atmosphere was so comfortable.',
  '\n        メイク方法も一つひとつ詳しく教えてくださり、自分の色が分かってスッキリしました。服のスタイルからアクセサリーまで一つずつ選んでくださって良かったです！何を聞いても親切に答えてくださり、雰囲気も良くてリラックスできました。',
  '\n        化妝方法也一步一步詳細教我，找到自己的顏色真的豁然開朗。從穿搭風格到飾品都一一幫我挑，太棒了！什麼問題都親切解答，氣氛也很好很放鬆。')
t('\n        잘 받고 갑니당~~ 화장법 배우러 또 올게요!!',
  "\n        Thank you — I'll be back for a makeup lesson!",
  '\n        ありがとうございました！メイクを習いにまた来ます！',
  '\n        謝謝！還會再來學化妝！')
t('언니와 함께 와서 메이크업 방법 수업을 듣게 되었는데 원하는 스타일로 자연스럽게 잘 알려주셨어요!!!',
  'Came with my older sister for a makeup lesson, and our teacher showed us exactly the looks we wanted in a natural, easy way!',
  '姉と一緒にメイクレッスンを受けました。希望のスタイルを自然に分かりやすく教えてくださいました！',
  '和姐姐一起來上彩妝課，老師依照我們想要的風格，教得很自然又清楚！')
t('\n        처음 메이크업을 하는데 브러쉬 사용 방법부터 차근차근 잘 알려주시고 피드백도 매우 잘해주셔서 좋았습니다!',
  "\n        It was my first time doing makeup, and she patiently walked me through everything, starting with how to use brushes, and gave great feedback!",
  '\n        メイク初心者でしたが、ブラシの使い方から順番に教えてくださり、フィードバックもとても的確でした！',
  '\n        第一次化妝，從刷具用法開始一步步教，回饋也非常到位！')

# ---------- ABOUT / PRINCIPLE ----------
t('"학술적 이론과 현장 감각이 만든 프라이빗 컨설팅"',
  '"Private consulting built on academic theory and real-world experience"',
  '「学術理論と現場感覚から生まれたプライベートコンサルティング」',
  '「以學術理論與現場經驗打造的私人諮詢」')
t('진정한 퍼스널 이미지는 단편적인 톤 구분으로 완성되지 않습니다.\n\n헤어와 메이크업, 타고난 골격과 체형 라인까지 완벽한 조화를 이룰 때 비로소 당신만의 독보적인 분위기가 완성됩니다.\n\n헤어 석사 · 메이크업 박사 대표원장의 1:1 밀착 디렉팅으로 당신 본연의 품격을 찾아드립니다.',
  'A true personal image takes more than simply sorting you into a color tone.\n\nYour own unmistakable aura comes together only when your hair, makeup, natural bone structure and body line are all in harmony.\n\nWith 1:1, hands-on guidance from our director — MA in hair, PhD in makeup — we help you discover the elegance that is truly yours.',
  '本当のパーソナルイメージは、トーンを分けるだけでは完成しません。\n\nヘアとメイク、生まれ持った骨格や体型ラインまでが調和したとき、はじめてあなただけの唯一無二の雰囲気が完成します。\n\nヘア修士・メイク博士の代表院長が1対1でじっくりディレクションし、あなた本来の品格を引き出します。',
  '真正的個人形象，不是單純區分色調就能完成。\n\n當髮型與妝容、天生骨架與體型線條都達到和諧時，才能完成專屬於你的獨特氛圍。\n\n由美髮碩士・彩妝博士代表院長一對一貼身指導，找出你與生俱來的氣質。')
t('당신을 그리다의 ', 'Our ', 'Draw Your Lifeの', 'Draw Your Life 的')
t('3가지', '3', '3つの', '3項')
t(' 약속', ' promises', 'お約束', '承諾')
t('소중한 당신의 퍼스널 이미지를 위해 타협하지 않는 원칙입니다.',
  'Principles we never compromise on when it comes to your personal image.',
  '大切なあなたのパーソナルイメージのために、妥協しない原則です。',
  '為了你珍貴的個人形象，絕不妥協的原則。')
t('현장 경험에서 나오는 실전 스타일링', 'Practical styling from real-world experience', '現場経験から生まれる実践スタイリング', '源自現場經驗的實戰造型')
t('헤어디자이너와 메이크업 아티스트를 모두 거친 15년 노하우로, 실제 적용 가능한 현실적이고 완벽한 이미지 변신을 끌어냅니다.',
  'With 15 years of experience as both a hair designer and a makeup artist, we bring out a realistic, complete transformation you can actually use every day.',
  'ヘアデザイナーとメイクアップアーティストの両方を経験した15年のノウハウで、実際に取り入れられる現実的で完璧なイメージチェンジを引き出します。',
  '憑藉同時擔任過髮型設計師與彩妝師的15年經驗，打造真正能運用在日常、務實又完美的形象改造。')
t('메이크업 박사 · 헤어 석사 원장의 초정밀 분석', 'Ultra-precise analysis by a PhD in makeup & MA in hair', 'メイク博士・ヘア修士による超精密分析', '彩妝博士・美髮碩士院長的超精密分析')
t('전문적인 학술 데이터와 6500K 정밀 조명, 특허받은 교구 사용, 국내 최초 홍채 패턴 측정까지 동원하여 완벽에 가까운 오진단 0%를 지향합니다.',
  "Using academic data, precision 6500K lighting, patented diagnostic tools and Korea's first iris pattern measurement, we aim for as close to zero misdiagnosis as possible.",
  '専門的な学術データ、6500Kの精密照明、特許取得の診断ツール、韓国初の虹彩パターン測定まで用いて、限りなく誤診0%を目指します。',
  '運用專業學術數據、6500K精密照明、專利診斷工具，以及韓國首創的虹膜紋路測量，力求接近零誤診。')
t('머리부터 발끝까지 완성되는 풀패키지 솔루션', 'A full-package solution, head to toe', '頭からつま先まで完成するフルパッケージ', '從頭到腳的全套解決方案')
t('퍼스널 컬러 진단을 시작으로 헤어 스타일링, 맞춤 메이크업 코칭, 파우치 정밀 점검, 패션 체형 분석까지 당신에게 최적화된 토탈 뷰티 맵을 제공합니다.',
  'From personal color analysis to hair styling, tailored makeup coaching, a detailed makeup bag check and body-type fashion analysis, we give you a total beauty map made just for you.',
  'パーソナルカラー診断をはじめ、ヘアスタイリング、オーダーメイドのメイクコーチング、ポーチの精密チェック、体型に合わせたファッション分析まで、あなたに最適化されたトータルビューティーマップをお渡しします。',
  '從個人色彩診斷開始，到髮型造型、客製彩妝指導、化妝包精密檢查、體型穿搭分析，提供為你量身打造的全方位美麗地圖。')

# ---------- 이미지 컨설팅: 구성 ----------
t('고객 맞춤 사전 상담', 'Personalized pre-consultation', 'お客様に合わせた事前カウンセリング', '客製化事前諮詢')
t('퍼스널컬러 3요소 신체색', '3-point natural coloring check', 'パーソナルカラーを決める3つの身体色', '個人色彩三要素')
t('(피부/눈동자/헤어컬러) 체크', '(skin / eyes / hair)', '（肌・瞳・髪色）チェック', '（膚色／瞳色／髮色）檢測')
t('퍼스널컬러 12계절 드레이핑 진단', '12-season personal color draping', 'パーソナルカラー12シーズン・ドレープ診断', '12季型色布比色診斷')
t('색조 메이크업 제품 추천', 'Makeup product recommendations', 'カラーメイクアイテムの提案', '彩妝產品推薦')
t('립 컬러 테스트', 'Lip color test', 'リップカラーテスト', '唇色測試')
t('자체 제작 진단결과지 +', 'Custom results sheet +', 'オリジナル診断結果シート＋', '自製診斷結果單＋')
t('쇼핑 참고용 컬러 카드 제공', 'color card for shopping', '買い物用カラーカード', '購物用色卡')
t('패션스타일링 추천 + 쥬얼리 추천', 'Fashion styling + jewelry', 'ファッション＋ジュエリー提案', '穿搭＋飾品推薦')
t('헤어 디자인 + 컬러 추천', 'Hair design + color', 'ヘアデザイン＋カラー提案', '髮型＋髮色推薦')
t('아이브로우 디자인 + 컬러 추천', 'Brow design + color', '眉デザイン＋カラー提案', '眉型＋眉色推薦')
t('네일 디자인 + 컬러 추천', 'Nail design + color', 'ネイルデザイン＋カラー提案', '美甲款式＋顏色推薦')
t('렌즈 디자인 + 컬러 추천', 'Contact lens design + color', 'カラコンデザイン＋カラー提案', '彩色隱形眼鏡款式＋顏色推薦')
t('안경 디자인 + 컬러 추천', 'Eyeglass frames + color', 'メガネデザイン＋カラー提案', '眼鏡款式＋顏色推薦')
t('이미지에 어울리는 향수 추천', 'Fragrance that suits your image', 'イメージに合う香水の提案', '適合形象的香水推薦')
t('톤별 맞춤 가이드 제공', 'Custom guide for your color type', 'トーン別ガイド', '色調專屬指南')
t('메이크업 파우치 진단', 'Makeup bag check', 'メイクポーチ診断', '化妝包診斷')
t('얼굴 이목구비 골격 AI 정밀 분석', 'AI analysis of facial features & bone structure', '顔パーツ・骨格のAI精密分析', '臉部五官骨架AI精密分析')
t('얼굴형에 어울리는 메이크업 코칭', 'Makeup coaching for your face shape', '顔型に合うメイクコーチング', '適合臉型的彩妝指導')
t('(치크 / 하이라이터 / 쉐딩)', '(blush / highlighter / contour)', '（チーク・ハイライト・シェーディング）', '（腮紅／打亮／修容）')
t('체형 골격 AI 정밀 분석', 'AI body type analysis (bone structure)', '体型骨格のAI精密分析', '體型骨架AI精密分析')
t('체형에 알맞는 패션 스타일링 코칭', 'Fashion styling coaching for your body type', '体型に合うファッションコーチング', '適合體型的穿搭指導')
t('(디자인 / 컬러 / 소재)', '(design / color / fabric)', '（デザイン・カラー・素材）', '（款式／顏色／材質）')
t('이미지메이킹 토탈 가이드 제공', 'Complete personal image guide', 'イメージメイキング・トータルガイド', '形象打造全方位指南')
t('* 추가 옵션 선택', '* Add-on options', '* 追加オプション', '* 加購選項')
t('패션 스타일링 추천 + 쥬얼리 추천', 'Fashion styling + jewelry', 'ファッション＋ジュエリー提案', '穿搭＋飾品推薦')
t('얼굴형에 어울리는 넥라인 추천', 'Necklines for your face shape', '顔型に合うネックライン提案', '適合臉型的領口推薦')
t('옵션 당 20,000원', '₩20,000 per option', '1オプションにつき ₩20,000', '每項 ₩20,000')
t('얼굴 이목구비 골격 정밀 분석', 'Facial features & bone structure analysis', '顔パーツ・骨格の精密分析', '臉部五官骨架精密分析')
t('체형 골격 정밀 분석', 'Body type analysis (bone structure)', '体型骨格の精密分析', '體型骨架精密分析')
t('PDF만 제공', 'PDF report only', 'PDFでのご提供のみ', '僅提供PDF')
t('옵션 당 50,000원', '₩50,000 per option', '1オプションにつき ₩50,000', '每項 ₩50,000')
t('뷰티전공 대학교수 대표원장 직강 ', 'Taught by our director, a beauty professor: ', '美容専攻の大学教授・代表院長が直接指導 ', '美容系大學教授代表院長親授 ')
t('‘메이크업 클래스’', '“Makeup Class”', '「メイクレッスン」', '「彩妝課程」')
t('1인 (80분)', '1 person (80 min)', '1名（80分）', '1人（80分鐘）')
t('2인 (110분)', '2 people (110 min)', '2名（110分）', '2人（110分鐘）')
t('180,000원', '₩180,000', '₩180,000', '₩180,000')
t('160,000원', '₩160,000', '₩160,000', '₩160,000')
t('320,000원', '₩320,000', '₩320,000', '₩320,000')
t('290,000원', '₩290,000', '₩290,000', '₩290,000')

# ---------- 가격표 공통 ----------
t('컨설팅', 'Course', 'コース', '方案')
t('인원', 'Guests', '人数', '人數')
t('소요시간(분)', 'Time (min)', '所要時間（分）', '時間（分鐘）')
t('가격', 'Price', '料金', '價格')
t('1인', '1', '1名', '1人')
t('2인', '2', '2名', '2人')
t('3인', '3', '3名', '3人')
t('1인 11만원', '₩110,000 / person', '1名あたり ₩110,000', '每人 ₩110,000')
t('1인 10.5만원', '₩105,000 / person', '1名あたり ₩105,000', '每人 ₩105,000')
t('1인 8.5만원', '₩85,000 / person', '1名あたり ₩85,000', '每人 ₩85,000')
t('1인 20만원', '₩200,000 / person', '1名あたり ₩200,000', '每人 ₩200,000')
t('1인 18만원', '₩180,000 / person', '1名あたり ₩180,000', '每人 ₩180,000')
t('1인 16만원', '₩160,000 / person', '1名あたり ₩160,000', '每人 ₩160,000')
t('1인 14만원', '₩140,000 / person', '1名あたり ₩140,000', '每人 ₩140,000')
t('1인 30만원', '₩300,000 / person', '1名あたり ₩300,000', '每人 ₩300,000')
t('1인 28만원', '₩280,000 / person', '1名あたり ₩280,000', '每人 ₩280,000')
t('1인 23만원', '₩230,000 / person', '1名あたり ₩230,000', '每人 ₩230,000')
t('※ 4인 이상 기업·단체 예약 및 미디어 협업은 별도 문의 바랍니다.',
  '※ For corporate or group bookings of 4 or more, and media collaborations, please contact us.',
  '※ 4名以上の企業・団体予約やメディアとのコラボは別途お問い合わせください。',
  '※ 4人以上企業・團體預約及媒體合作，請另行洽詢。')

# ---------- 이미지 컨설팅 FAQ ----------
t('DRAW · YOUR · LIFE는 어떻게 다른가요?', 'How are DRAW, YOUR and LIFE different?', 'DRAW・YOUR・LIFEの違いは？', 'DRAW・YOUR・LIFE 有什麼不同？')
t('뒤로 갈수록 앞 과정을 포함하는 구조입니다. ', 'Each course includes everything in the one before it. ', '後のコースほど前のコースの内容を含みます。', '後面的方案包含前面方案的所有內容。')
t('는 12계절 드레이핑 진단과 색조 제품·립 컬러 추천, 진단결과지와 컬러 카드까지. ',
  ' covers 12-season draping, makeup product and lip color recommendations, plus your results sheet and color card. ',
  'は12シーズンのドレープ診断、カラーメイクアイテム・リップカラーの提案、診断結果シートとカラーカードまで。',
  '包含12季型色布比色診斷、彩妝產品與唇色推薦、診斷結果單與色卡。')
t('는 여기에 패션 스타일링·쥬얼리, 헤어·아이브로우·네일 디자인, 렌즈·안경 디자인, 향수 추천과 메이크업 파우치 진단이 더해집니다. ',
  ' adds recommendations for fashion and jewelry, hair, brows, nails, contact lenses, eyeglasses and fragrance, plus a makeup bag check. ',
  'はそこにファッション・ジュエリー、ヘア・眉・ネイルデザイン、カラコン・メガネデザイン、香水の提案とメイクポーチ診断が加わります。',
  '再加上穿搭與飾品、髮型・眉型・美甲設計、彩色隱形眼鏡・眼鏡款式、香水推薦與化妝包診斷。')
t('는 얼굴 골격과 체형 골격 AI 정밀 분석, 메이크업 코칭과 패션 스타일링 코칭까지 포함한 토탈 과정입니다.',
  ' is the complete course, adding AI analysis of your facial bone structure and body type, plus makeup and fashion styling coaching.',
  'は顔の骨格と体型骨格のAI精密分析、メイクコーチングとファッションコーチングまで含むトータルコースです。',
  '是全方位方案，再加上臉部與體型骨架AI精密分析、彩妝指導與穿搭指導。')
t('퍼스널컬러 진단, 시간과 가격은 어떻게 되나요?', 'How long does personal color analysis take, and how much is it?', '診断の所要時間と料金は？', '個人色彩診斷的時間和價格是？')
t('1인 기준 DRAW 40분 11만원, YOUR 80분 20만원, LIFE 110분 30만원입니다. 인원이 늘수록 1인당 금액이 내려가서 DRAW 3인은 1인 8.5만원입니다. 4인 이상 기업·단체 예약은 별도 문의 주세요. 인원별 표는 위 가격 안내에 정리해두었습니다.',
  'For one person: DRAW 40 min ₩110,000, YOUR 80 min ₩200,000, LIFE 110 min ₩300,000. The more people, the lower the price per person — DRAW for 3 is ₩85,000 each. For groups of 4 or more, please contact us. See the price table above for details.',
  '1名の場合、DRAW 40分 ₩110,000、YOUR 80分 ₩200,000、LIFE 110分 ₩300,000です。人数が増えるほど1名あたりの料金が下がり、DRAW 3名なら1名あたり ₩85,000です。4名以上の企業・団体予約は別途お問い合わせください。人数別の料金は上の表をご覧ください。',
  '1人價格：DRAW 40分鐘 ₩110,000、YOUR 80分鐘 ₩200,000、LIFE 110分鐘 ₩300,000。人數越多每人越便宜，DRAW 3人每人 ₩85,000。4人以上團體預約請另行洽詢。各人數價格請見上方價目表。')
t('2인 이상 함께 예약하면 어떻게 진행되나요?', 'How does it work if we book together?', '2名以上で予約するとどうなりますか？', '2人以上一起預約會怎麼進行？')
t('같은 시간에 함께 진행되며 인원이 늘수록 1인당 금액이 내려갑니다. DRAW·YOUR·LIFE 모두 최대 3인까지 예약하실 수 있고, 4인 이상 기업·단체 예약은 별도 문의 주세요.',
  'You all go through the session together at the same time, and the per-person price drops as the group grows. DRAW, YOUR and LIFE can each be booked for up to 3 people; for 4 or more, please contact us.',
  '同じ時間に一緒に進行し、人数が増えるほど1名あたりの料金が下がります。DRAW・YOUR・LIFEいずれも最大3名まで予約でき、4名以上は別途お問い合わせください。',
  '同一時段一起進行，人數越多每人越便宜。DRAW・YOUR・LIFE 皆最多可預約3人，4人以上請另行洽詢。')
t('진단 결과는 어떤 형태로 받나요?', 'What do I take home?', '診断結果はどのような形で受け取れますか？', '診斷結果會以什麼形式提供？')
t('자체 제작한 진단 결과지와, 쇼핑할 때 들고 다니며 참고할 수 있는 컬러 카드를 드립니다. YOUR 컨설팅은 톤별 맞춤 가이드(PDF)를 추가로 보내드리고, LIFE 컨설팅은 이미지메이킹 토탈 가이드(PDF)까지 보내드립니다.',
  'You receive our own results sheet and a color card to carry and refer to while shopping. With YOUR, we also send you a custom guide for your color type (PDF), and with LIFE, a complete personal image guide (PDF) as well.',
  'オリジナルの診断結果シートと、お買い物の際に持ち歩いて参考にできるカラーカードをお渡しします。YOURコンサルではトーン別ガイド（PDF）を追加でお送りし、LIFEコンサルではイメージメイキング・トータルガイド（PDF）までお送りします。',
  '提供自製的診斷結果單，以及購物時可隨身攜帶參考的色卡。YOUR 諮詢另外寄送色調專屬指南（PDF），LIFE 諮詢則再加送形象打造全方位指南（PDF）。')
t('결혼 준비 중이라면,', 'Getting married?', '結婚準備中なら、', '正在準備婚禮的話，')
t('드레스 투어 전에 내 컬러부터', 'Find your colors before you go dress shopping', 'ドレス選びの前に、まず自分のカラーを', '挑婚紗之前，先找到自己的顏色')
t('퍼스널컬러 진단 + 웨딩 컨설팅을 한 번에. 2부 드레스, 신랑 예복, 티아라·부케·쥬얼리, 스드메 견적 비교 노하우까지 유부선배가 함께 준비해드려요.',
  'Personal color analysis + wedding consulting in one session. Reception dress, groom’s suit, tiara, bouquet and jewelry — even tips on comparing studio, dress and makeup package quotes — from someone who has been through it herself.',
  'パーソナルカラー診断＋ウェディングコンサルを一度に。お色直しドレス、新郎の衣装、ティアラ・ブーケ・ジュエリー、スタジオ・ドレス・メイクの見積もり比較のコツまで、結婚経験のある先輩が一緒に準備します。',
  '個人色彩診斷＋婚禮諮詢一次完成。第二套禮服、新郎禮服、皇冠・捧花・珠寶，連婚紗攝影・禮服・新秘方案的比價訣竅，由已婚過來人陪你一起準備。')
t('웨딩 컨설팅 자세히 보기 →', '@@ASK_WEDDING@@ →', '@@ASK_WEDDING@@ →', '@@ASK_WEDDING@@ →')
t('신랑+신부 2인', 'Bride + groom (2)', '新郎＋新婦 2名', '新郎＋新娘 2人')
t('38만원', '₩380,000 total', '計 ₩380,000', '共 ₩380,000')
t('신부 1인', 'Bride only', '新婦のみ 1名', '新娘 1人')
t('27만원', '₩270,000', '₩270,000', '₩270,000')
t('※ 신부님 1인 컨설팅은 가능하지만, 신랑님 1인 컨설팅은 진행하지 않습니다. ',
  '※ The bride may come alone, but we do not offer groom-only sessions.',
  '※ 新婦様お一人でのコンサルは可能ですが、新郎様お一人でのコンサルは行っておりません。',
  '※ 新娘可單獨諮詢，但不提供新郎單獨諮詢。')
t('웨딩 컨설팅은 어떻게 진행되나요?', 'How does wedding consulting work?', 'ウェディングコンサルはどのように進みますか？', '婚禮諮詢怎麼進行？')
t('퍼스널컬러 진단과 웨딩 컨설팅을 한 번에 진행합니다. 드레이핑 진단으로 베스트·세컨드·워스트 컬러를 찾고, 그 결과를 기준으로 촬영·본식·2부 드레스, 신랑 예복과 넥타이, 티아라·베일·쥬얼리·부케·네일, 한복, 허니문 커플룩까지 컨설팅합니다. 스드메 견적 비교 등 웨딩 준비 노하우도 함께 알려드립니다. 신랑+신부 2인 110분 38만원, 신부 1인 80분 27만원이며, 신부만 오셔도 신랑님 퍼스널컬러 진단을 제외한 나머지는 모두 진행됩니다. 웨딩 스타일링은 신부님을 기준으로 정해지기 때문에 신랑님 1인 컨설팅은 진행하지 않습니다. ',
  'Personal color analysis and wedding consulting are done in one session. Draping identifies your best, second-best and worst colors, and based on that we advise on dresses for the photo shoot, ceremony and reception, the groom’s suit and tie, tiara, veil, jewelry, bouquet and nails, hanbok, and matching honeymoon outfits. We also share wedding-prep tips, such as how to compare studio, dress and makeup quotes. Bride + groom: 110 min, ₩380,000. Bride only: 80 min, ₩270,000. If only the bride comes, everything except the groom’s personal color analysis is still covered. Because wedding styling is built around the bride, we do not offer groom-only sessions.',
  'パーソナルカラー診断とウェディングコンサルを一度に行います。ドレープ診断でベスト・セカンド・ワーストカラーを見つけ、その結果をもとに前撮り・挙式・お色直しのドレス、新郎の衣装とネクタイ、ティアラ・ベール・ジュエリー・ブーケ・ネイル、韓服、ハネムーンのペアルックまでご提案します。スタジオ・ドレス・メイクの見積もり比較など、結婚準備のコツもお伝えします。新郎＋新婦2名 110分 ₩380,000、新婦1名 80分 ₩270,000です。新婦様だけのご来店でも、新郎様のパーソナルカラー診断以外はすべて行います。ウェディングのスタイリングは新婦様を基準に決まるため、新郎様お一人でのコンサルは行っておりません。',
  '個人色彩診斷與婚禮諮詢一次進行。透過色布比色找出最佳・次佳・最不適合的顏色，並以此為基準，針對拍婚紗照・婚禮當天・第二套禮服的禮服挑選、新郎禮服與領帶、皇冠・頭紗・珠寶・捧花・美甲、韓服，以及蜜月情侶裝提供建議。也會分享婚紗攝影・禮服・新秘方案比價等備婚訣竅。新郎＋新娘2人 110分鐘 ₩380,000，新娘1人 80分鐘 ₩270,000；只有新娘來，也會進行除新郎個人色彩診斷以外的所有內容。婚禮造型以新娘為基準，因此不提供新郎單獨諮詢。')

# ---------- 메이크업 ----------
t('메이크업 클래스 + 얼굴 골격진단', 'Makeup Class + Facial Bone Structure Analysis', 'メイクレッスン＋顔の骨格診断', '彩妝課程＋臉部骨架診斷')
t("'당신을 그리다'만의 독보적인 메이크업클래스", 'A makeup class you’ll only find at Draw Your Life', 'Draw Your Lifeだけの唯一無二のメイクレッスン', 'Draw Your Life 獨有的彩妝課程')
t("유튜브나 SNS를 보고 똑같이 따라 해도 내 얼굴에는 어색했던 경험, 다들 한 번쯤 있으실 겁니다. 사람마다 골격, 피부톤, 이목구비의 비대칭 정도가 모두 다르기 때문에 남들과 똑같은 화장법이 아닌 '나에게 맞는 화장법'은 따로 있습니다.",
  'Most of us have copied a look from YouTube or social media step by step, only to find it looked off on our own face. Bone structure, skin tone and facial asymmetry differ from person to person, so rather than doing your makeup like everyone else, you need the techniques that work for your face.',
  'YouTubeやSNSを見て同じようにまねしても、自分の顔だと何だか違和感があった…そんな経験、一度はありますよね。骨格、肌トーン、パーツの左右差は人それぞれ違うので、みんなと同じメイクではなく「自分に合うメイク」があるのです。',
  '看著YouTube或社群一模一樣跟著畫，放在自己臉上卻很違和——相信大家都有過這種經驗。每個人的骨架、膚色、五官不對稱程度都不同，所以真正適合你的不是和別人一樣的畫法，而是「適合自己的畫法」。')
t('밀착 메이크업 레슨 커리큘럼', 'Hands-on makeup lesson curriculum', 'マンツーマン・メイクレッスンのカリキュラム', '貼身彩妝課程內容')
t('기초 스킨케어부터 색조 활용까지, 내 얼굴을 제대로 이해하고 단점을 커버하는 방법을 1:1로 디테일하게 배웁니다.',
  'From basic skincare to color cosmetics, you’ll learn in detailed 1:1 sessions how to truly understand your face and cover the areas you’d like to soften.',
  '基礎スキンケアからカラーメイクの使い方まで、自分の顔を正しく理解し、気になる部分をカバーする方法を1対1で細かく学びます。',
  '從基礎保養到彩妝運用，一對一細緻學習真正了解自己的臉、修飾缺點的方法。')
t('사전 상담 및 이미지 컨설팅', 'Pre-consultation & image consulting', '事前カウンセリング＆イメージコンサル', '事前諮詢及形象諮詢')
t('원하시는 이미지와 평소 메이크업 고민을 분석하여 맞춤형 레슨 방향을 설정합니다.',
  'We look at the image you want and your everyday makeup concerns to set the direction of your personalized lesson.',
  'ご希望のイメージと普段のメイクのお悩みを分析し、あなたに合わせたレッスンの方向性を決めます。',
  '分析你想要的形象和平時的化妝煩惱，設定專屬的課程方向。')
t('고민 예시', 'Common concerns', 'お悩みの例', '常見煩惱')
t('무너지지 않는 스킨케어 및 베이스', 'Skincare & base that lasts', '崩れないスキンケア＆ベース', '不脫妝的保養與底妝')
t('화장의 완성도를 결정하는 올바른 스킨케어 방법과 얇고 밀착력 있는 베이스 스킬을 알려드립니다.',
  'Learn the right skincare routine — the key to how your makeup turns out — and techniques for a thin, skin-hugging base that stays put.',
  'メイクの仕上がりを左右する正しいスキンケア方法と、薄く密着するベースのテクニックをお伝えします。',
  '教你決定妝容完成度的正確保養方法，以及輕薄服貼的底妝技巧。')
t('얼굴형 맞춤 윤곽 및 브로우 메이크업', 'Contouring & brows for your face shape', '顔型に合わせた輪郭＆眉メイク', '依臉型打造的修容與眉妝')
t('내 얼굴 골격에 맞는 섀딩과 하이라이터로 입체감을 살리고, 인상을 결정짓는 가장 중요한 눈썹을 내 얼굴형에 맞게 다듬고 자연스럽게 그리는 방법을 코칭합니다.',
  'Add dimension with contour and highlighter that match your bone structure, and learn to shape and naturally draw your brows — the feature that defines your impression most — to suit your face shape.',
  '顔の骨格に合ったシェーディングとハイライトで立体感を出し、印象を決める一番大切な眉を顔型に合わせて整え、自然に描く方法をコーチングします。',
  '用適合自己骨架的修容與打亮做出立體感，並指導如何依臉型修整、自然畫出決定印象最重要的眉毛。')
t('눈매 교정 아이 메이크업', 'Eye makeup that refines your eye shape', '目元を整えるアイメイク', '修飾眼型的眼妝')
t('쌍꺼풀 유무, 꼬리 모양 등 눈의 형태에 맞춘 섀도우 영역 설정과 아이라인 그리는 법, 번지지 않는 마스카라 활용법을 밀착해서 알려드립니다.',
  'Up close, we show you where to place shadow for your eye shape (monolids or double lids, the shape of your outer corners), how to draw eyeliner, and how to apply mascara so it won’t smudge.',
  '一重・二重、目尻の形など、目の形に合わせたアイシャドウの範囲、アイラインの引き方、にじまないマスカラの使い方をマンツーマンで丁寧にお教えします。',
  '依單雙眼皮、眼尾形狀等眼型，貼身教你眼影範圍設定、眼線畫法，以及不暈妝的睫毛膏用法。')
t('생기를 더하는 립 &amp; 블러셔', 'Lips &amp; blush for a fresh glow', '血色を足すリップ＆チーク', '增添氣色的唇妝與腮紅')
t('얼굴에 자연스러운 혈색과 입체감을 부여하는 블러셔 위치를 잡고, 내 입술 형태에 맞는 립 메이크업 연출법을 배웁니다.',
  'Find the blush placement that gives your face natural color and dimension, and learn lip makeup that suits the shape of your lips.',
  '顔に自然な血色と立体感を与えるチークの位置を決め、唇の形に合ったリップメイクの方法を学びます。',
  '找到能帶來自然氣色與立體感的腮紅位置，學習適合自己唇形的唇妝畫法。')
t('이런 점이 다릅니다', 'What makes it different', 'ここが違います', '我們的不同之處')
t('대학교수의 맞춤형 눈높이 교육', 'Taught at your level by a university professor', '大学教授がレベルに合わせて指導', '大學教授依你的程度量身教學')
t('화장을 한 번도 해보지 않은 초보자도 쉽게 이해할 수 있도록, 브러쉬 잡는 법부터 힘을 빼는 방법까지 전문 용어 없이 아주 일상적인 언어로 원리를 설명해 드립니다. 대표원장이 얼굴 한쪽을 시연하며 가르쳐드리면, 나머지 반쪽은 직접 따라해보면서 메이크업 스킬을 익힙니다.',
  'So that even someone who has never worn makeup can follow, we explain the principles in everyday language without jargon — from how to hold a brush to how to keep a light touch. Our director demonstrates on one half of your face, and you do the other half yourself to build the skill.',
  'メイクを一度もしたことがない初心者でも分かりやすいよう、ブラシの持ち方から力の抜き方まで、専門用語を使わず日常の言葉で原理を説明します。代表院長が顔の片側を実演しながら教え、もう片側はご自身でまねして描きながらスキルを身につけます。',
  '就算是從沒化過妝的新手也能輕鬆理解，從怎麼握刷具到怎麼放輕力道，都不用專業術語、以日常語言說明原理。代表院長示範半邊臉，另外半邊由你親手跟著畫，學會彩妝技巧。')
t('철저한 맞춤 교육', 'Fully tailored to you', '徹底したオーダーメイド指導', '徹底客製化教學')
t('고객님 얼굴을 파악하여 장점은 극대화하고 단점은 자연스럽게 보완하는 스킬을 전수합니다.',
  'We study your face and pass on the skills to maximize your strengths and naturally balance what you’d like to soften.',
  'お客様の顔を把握し、長所は最大限に、短所は自然にカバーするスキルをお伝えします。',
  '掌握你的臉部特點，傳授放大優點、自然修飾缺點的技巧。')
t('나만의 아름다움을 그리는 시간, 당신을그리다에서 평생 활용 가능한 진짜 메이크업 스킬을 배워가시길 바랍니다.',
  'A time to draw your own beauty. At Draw Your Life, we hope you take home real makeup skills you can use for life.',
  'あなただけの美しさを描く時間。Draw Your Lifeで、一生使える本物のメイクスキルを身につけてください。',
  '描繪專屬於你的美的時光，在 Draw Your Life 學會受用一生的真正彩妝技巧。')
t('메이크업 클래스', 'Makeup Class', 'メイクレッスン', '彩妝課程')
t('클래스', 'Class', 'クラス', '課程')
t('1Day × 3회', '1Day × 3', '1Day × 3回', '1Day × 3次')
t('입시반', 'Entrance exam prep', '美容系入試対策クラス', '美容升學考試班')
t('최대 4인', 'Up to 4', '最大4名', '最多4人')
t('개별 문의', 'Ask us', 'お問い合わせ', '請洽詢')
t('※ 3Day 클래스의 소요시간은 ', '※ For the 3Day class, the time shown is ', '※ 3Dayクラスの所要時間は', '※ 3Day 課程標示的時間為')
t('1회당', 'per session', '1回あたり', '每次')
t(' 시간입니다. (1Day 과정 × 3회)', '. (1Day course × 3 sessions)', 'の時間です。（1Dayコース × 3回）', '上課時間。（1Day 課程 × 3次）')
t('* 이미지 컨설팅과 함께 예약 시', '* When booked with image consulting', '* イメージコンサルと一緒に予約する場合', '* 與形象諮詢一起預約時')
t('메이크업 클래스는 컨설팅과 별개인가요?', 'Is the makeup class separate from consulting?', 'メイクレッスンはコンサルとは別ですか？', '彩妝課程和諮詢是分開的嗎？')
t('별도 과정이며 뷰티전공 대학교수인 대표원장이 직접 진행합니다. 상담으로 고민을 먼저 파악한 뒤 수업하는데, 원장이 시연하면 바로 따라 실습하고 다시 시연하고 실습하는 식으로 구간을 나눠 디테일하게 진도를 나갑니다. 이미지 컨설팅과 함께 예약하시면 할인이 적용돼 두 가지를 같이 신청하시는 분이 가장 많습니다.',
  'Yes, it is a separate course taught personally by our director, a beauty professor. We start by understanding your concerns, then go step by step in detail: the director demonstrates, you practice right away, and we repeat. Booking it together with image consulting gets you a discount, so most guests do both.',
  '別のコースで、美容専攻の大学教授である代表院長が直接担当します。まずカウンセリングでお悩みを把握してからレッスンを行い、院長が実演したらすぐに実習、また実演して実習…と区切りながら細かく進めます。イメージコンサルと一緒に予約すると割引が適用されるため、両方お申し込みになる方が一番多いです。',
  '是另外的課程，由美容系大學教授代表院長親自授課。先透過諮詢了解你的煩惱再上課，院長示範後馬上跟著練習，再示範、再練習，分段細緻地進行。與形象諮詢一起預約可享折扣，所以大多數人都會兩者一起報名。')

# ---------- 공통 FAQ ----------
t('진단 전에 화장을 하고 가도 되나요?', 'Can I wear makeup to my session?', '診断の前にメイクをして行ってもいいですか？', '診斷前可以化妝嗎？')
t('정확한 진단을 위해 ', 'For an accurate analysis, please come ', '正確な診断のため、', '為了準確診斷，請')
t('노메이크업', 'without makeup', 'ノーメイク', '素顏')
t('으로 방문해 주셔야 합니다. 피부톤을 커버하는 톤업 선크림도 바르지 말아 주세요. 매장에서 화장을 지우실 경우 그 시간이 컨설팅 시간에 포함되니, 미리 지우고 오시면 진단에 온전히 쓰실 수 있습니다.',
  '. Please also skip tone-up sunscreen, which masks your natural skin tone. If you remove makeup at the studio, that time counts toward your session, so coming bare-faced lets you use the full time for your analysis.',
  'でお越しください。肌トーンをカバーするトーンアップ日焼け止めも塗らないでください。店内でメイクを落とす場合はその時間もコンサル時間に含まれるため、事前に落としてお越しいただくと、時間をすべて診断に使えます。',
  '前來。也請不要擦會修飾膚色的提亮防曬。若在店內卸妝，卸妝時間會算在諮詢時間內，事先卸好再來就能把時間完整用在診斷上。')
t('강서구 마곡 어디에 있나요? 예약은 어떻게 하나요?', 'Where are you and how do I book?', '場所と予約方法は？', '地點在哪裡？如何預約？')
t('서울 강서구 마곡중앙6로 21, 711호입니다. 네이버 예약으로 접수하며 평일 11:00~19:00, 주말·공휴일 11:00~17:00 운영합니다. 대표원장 대학 강의 일정에 따라 변동될 수 있습니다.',
  '@@LOCATION@@', '@@LOCATION@@', '@@LOCATION@@')

# ---------- 예약 ----------
t('나만을 위한 퍼스널 이미지, 지금 시작해보세요', 'Start your personal image journey today', 'あなただけのパーソナルイメージ、今日からはじめてみませんか', '專屬你的個人形象，現在就開始')
t('당신의 아름다움을 그리는 첫 걸음', 'The first step to drawing your beauty', 'あなたの美しさを描く第一歩', '描繪你的美的第一步')
t('평일', 'Weekdays', '平日', '平日')
t('주말, 공휴일', 'Weekends & holidays', '土日・祝日', '週末・國定假日')
t('* 대표원장 대학 강의 일정에 따라 변동될 수 있습니다',
  "* Hours may change depending on the director's university teaching schedule",
  '* 代表院長の大学の講義スケジュールにより変更になる場合があります',
  '* 可能依代表院長的大學授課行程調整')
t('당신을 그리다는 미용예술학 학사·석사·박사 학위를 모두 보유한 뷰티전공 현직 대학교수, 2016년~ 퍼스널컬러 연구 및 KCI 등재 논문 저자인 대표원장 박현정이 직접 진단합니다.',
  'At Draw Your Life (당신을 그리다), every diagnosis is done personally by Director Park Hyun-jeong — a university professor of beauty with bachelor’s, master’s and doctoral degrees in beauty arts, researching personal color since 2016 and author of KCI-indexed papers.',
  'Draw Your Life（당신을 그리다）では、美容芸術学の学士・修士・博士を持つ現役の美容専攻大学教授で、2016年からパーソナルカラーを研究しKCI掲載論文を執筆している代表院長パク・ヒョンジョンが直接診断します。',
  '在 Draw Your Life（당신을 그리다），由擁有美容藝術學學士・碩士・博士學位的美容系現任大學教授、2016年起研究個人色彩並撰寫KCI收錄論文的代表院長 Park Hyun-jeong 親自診斷。')
t("당신을 그리다의 세컨드 브랜드, 눈썹 아트메이크업 전문 '닥터뷰티랩'이 궁금하다면 →",
  'Curious about Dr. Beauty Lab, our sister brand specializing in semi-permanent brows? →',
  '姉妹ブランド・眉アートメイク専門「Dr. Beauty Lab」が気になる方はこちら →',
  '想了解我們的姊妹品牌——眉毛半永久專門店「Dr. Beauty Lab」嗎？→')

# ---------- 언어별 고정 문구 ----------
LANG = {
  'en': {
    'html_lang': 'en', 'og_locale': 'en_US', 'path': '/en/',
    'CTA': 'Message us on Instagram',
    'ASK_WEDDING': 'Ask about wedding consulting',
    'contact_url': 'https://www.instagram.com/drawyourlife_official/',
    'contact_note': 'Instagram @drawyourlife_official · You can message us in English.',
    'LOCATION': '711, 21 Magokjungang 6-ro, Gangseo-gu, Seoul (Magok, near Gimpo International Airport). Search “당신을 그리다” on Naver Map or Google Maps. Book via Instagram DM. Hours: weekdays 11:00–19:00, weekends & public holidays 11:00–17:00 (may vary with the director’s university teaching schedule).',
    'address_line': 'Address: 711, 21 Magokjungang 6-ro, Gangseo-gu, Seoul',
    'font_sans': None, 'font_serif': None,
  },
  'ja': {
    'html_lang': 'ja', 'og_locale': 'ja_JP', 'path': '/ja/',
    'CTA': 'InstagramのDMで予約・お問い合わせ',
    'ASK_WEDDING': 'ウェディングについてDMで相談',
    'contact_url': 'https://www.instagram.com/drawyourlife_official/',
    'contact_note': 'Instagram：@drawyourlife_official（日本語でお気軽にどうぞ）',
    'LOCATION': 'ソウル特別市江西区麻谷（マゴク）中央6路21 711号（金浦空港の近く）です。NAVER MapやGoogleマップで「당신을 그리다」と検索してください。ご予約はInstagramのDMで承ります。営業時間は平日11:00〜19:00、土日・祝日11:00〜17:00で、代表院長の大学の講義スケジュールにより変更になる場合があります。',
    'address_line': '住所：서울특별시 강서구 마곡중앙6로 21, 711호',
    'font_sans': 'Noto Sans JP', 'font_serif': 'Noto Serif JP',
  },
  'zh': {
    'html_lang': 'zh-Hant', 'og_locale': 'zh_TW', 'path': '/zh/',
    'CTA': 'Instagram 私訊預約・諮詢',
    'ASK_WEDDING': '私訊諮詢婚禮方案',
    'contact_url': 'https://www.instagram.com/drawyourlife_official/',
    'contact_note': 'Instagram：@drawyourlife_official（歡迎使用中文詢問）',
    'LOCATION': '地址為首爾市江西區 麻谷中央6路21號 711室（麻谷・金浦機場附近）。可在 Naver 地圖或 Google 地圖搜尋「당신을 그리다」。預約請透過 Instagram 私訊。營業時間平日 11:00–19:00，週末・國定假日 11:00–17:00，可能依代表院長的大學授課行程調整。',
    'address_line': '地址：서울특별시 강서구 마곡중앙6로 21, 711호',
    'font_sans': 'Noto Sans TC', 'font_serif': 'Noto Serif TC',
  },
}

# ---------- 현지어 검수 반영(원문 위치를 특정할 수 없던 항목) ----------
S['DRAW · YOUR · LIFE는 어떻게 다른가요?']['en'] = "What's the difference between DRAW, YOUR and LIFE?"
S['20,000건+']['ja'] = '20,000件以上'

# ---------- 2026-10-20 FAQ 교체 ----------
t('퍼스널컬러 진단, 어떤 곳에서 받아야 할까요?', 'Where should I get my personal color analysis?', 'パーソナルカラー診断は、どんなところで受けるべき？', '個人色彩診斷，該選擇什麼樣的地方？')
t('퍼스널컬러는 천을 대보며 눈으로 비교하는 진단이라 진단자의 경험과 조명 환경에 따라 결과가 달라집니다. 진단 경력, 일정한 조명, 세분화된 기준(12계절 등), 결과지 제공 여부를 확인해보세요. 당신을 그리다는 2016년부터 2만 건 이상 진단한 미용예술학 박사 대표원장이 6500K 정밀 조명 아래 12계절 드레이핑으로 직접 진단합니다.', 'Personal color analysis means comparing fabric drapes against your face by eye, so results depend on the analyst’s experience and the lighting. Check the analyst’s track record, consistent lighting, a detailed system (such as 12 seasons), and whether you get a results sheet. At Draw Your Life (당신을 그리다), our director — a PhD in beauty arts who has done more than 20,000 analyses since 2016 — analyzes you personally with 12-season draping under precision 6500K lighting.', 'パーソナルカラーは布を顔に当てて目で比べる診断なので、診断する人の経験や照明環境によって結果が変わります。診断歴、一定の照明、細かな分類（12シーズンなど）、診断結果シートがもらえるかを確認してみてください。Draw Your Life（당신을 그리다）では、2016年から2万件以上を診断してきた美容芸術学博士の代表院長が、6500Kの精密照明のもと12シーズンのドレープで直接診断します。', '個人色彩是把色布放在臉旁用肉眼比較的診斷，因此結果會因診斷者的經驗與照明環境而不同。建議確認診斷資歷、穩定的照明、細分的標準（如12季型），以及是否提供診斷結果單。在 Draw Your Life（당신을 그리다），由2016年起累計診斷超過2萬件的美容藝術學博士代表院長，在6500K精密照明下以12季型色布親自為你診斷。')
