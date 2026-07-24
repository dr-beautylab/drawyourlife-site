# 네이버 블로그 자동 포스팅 스크립트
# 실행: python scripts/naver_post.py
# 필요 환경변수: NAVER_ID, NAVER_PW, ANTHROPIC_API_KEY (GitHub Secrets에서 자동 주입됨)
#
# 주의: 네이버는 낯선 위치/기기에서의 로그인을 보안문자(캡차)나 2단계 인증으로
# 막을 수 있습니다. 이 경우 이 스크립트는 실패하며, 사람이 직접 로그인해서
# "본인 확인"을 한 번 해줘야 다시 정상화되는 경우가 많습니다.

import os
import json
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NAVER_ID = os.environ["NAVER_ID"]
NAVER_PW = os.environ["NAVER_PW"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

CONFIG_PATH = "blog/naver-config.json"
USED_PATH = "blog/naver-used-topics.json"


def read_json(path, fallback):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return fallback


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_post(config, topic):
    system_prompt = f"""당신은 "{config['siteName']}"의 네이버 블로그 글 작가입니다.
오로지 GEO(Generative Engine Optimization), SEO 관점에서만 작성합니다.
네이버 블로그 특성에 맞게, 정보성 콘텐츠이면서도 친근하고 자연스러운 후기/설명 톤으로 씁니다.
- 사실 기반, 구체적인 정보 위주 (모호한 미사여구 최소화)
- 업체명, 서비스명, 지역 키워드를 자연스럽게 반복 언급
- 소제목을 적절히 나눠 AI가 파싱하기 쉽게 작성
- 1500~2000자 분량
- 문단 사이는 빈 줄로 구분

업체 정보:
{config['businessInfo']}
"""
    user_prompt = f"""다음 주제로 네이버 블로그 글을 작성해줘: "{topic}"

아래 JSON 형식으로만 응답해줘 (다른 설명 없이 JSON만):
{{
  "title": "글 제목 (30자 이내)",
  "body": "본문 텍스트 (일반 텍스트, 문단 구분은 빈 줄로)"
}}"""

    res = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "Content-Type": "application/json",
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
        },
        json={
            "model": "claude-sonnet-5",
            "max_tokens": 3000,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        },
    )
    res.raise_for_status()
    text = "".join(block.get("text", "") for block in res.json()["content"])
    cleaned = text.replace("```json", "").replace("```", "").strip()
    return json.loads(cleaned)


def pick_topic(config, used):
    remaining = [t for t in config["topics"] if t not in used["usedTopics"]]
    if not remaining:
        used["usedTopics"] = []
        remaining = config["topics"][:]
    return remaining[0]


def login_naver(driver, wait):
    driver.get("https://nid.naver.com/nidlogin.login")
    # 네이버 로그인 페이지는 자동입력 방지를 위해 execute_script로 값 주입
    id_input = wait.until(EC.presence_of_element_located((By.ID, "id")))
    pw_input = driver.find_element(By.ID, "pw")
    driver.execute_script("arguments[0].value = arguments[1];", id_input, NAVER_ID)
    driver.execute_script("arguments[0].value = arguments[1];", pw_input, NAVER_PW)
    driver.find_element(By.ID, "log.login").click()
    time.sleep(3)

    if "캡차" in driver.page_source or "인증" in driver.title:
        raise RuntimeError(
            "네이버가 보안 인증(캡차/2단계 인증)을 요구했습니다. "
            "사람이 직접 브라우저로 로그인해서 '이 브라우저 기억하기'를 한 번 해줘야 합니다."
        )


def publish_post(driver, wait, blog_id, title, body):
    driver.get(f"https://blog.naver.com/{blog_id}?Redirect=Write&")
    time.sleep(3)

    # 새 글쓰기는 iframe(mainFrame) 안에서 진행됨
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mainFrame")))

    # "이어서 작성하기" 팝업이 뜨면 닫기
    try:
        driver.find_element(By.CSS_SELECTOR, ".se-popup-button-cancel").click()
        time.sleep(1)
    except Exception:
        pass

    title_area = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".se-title-text .se-text-paragraph"))
    )
    title_area.click()
    title_area.send_keys(title)

    body_area = driver.find_element(By.CSS_SELECTOR, ".se-main-container .se-text-paragraph")
    body_area.click()
    for paragraph in body.split("\n\n"):
        body_area.send_keys(paragraph)
        body_area.send_keys("\n")

    # 발행 버튼
    driver.find_element(By.CSS_SELECTOR, "button.publish_btn__m9KHH").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.confirm_btn__WEaBq").click()
    time.sleep(3)


def main():
    config = read_json(CONFIG_PATH, None)
    if not config:
        print("blog/naver-config.json 파일이 없습니다.")
        return

    used = read_json(USED_PATH, {"usedTopics": []})
    topic = pick_topic(config, used)
    print("선택된 주제:", topic)

    post = generate_post(config, topic)
    print("생성된 제목:", post["title"])

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        login_naver(driver, wait)
        publish_post(driver, wait, config["blogId"], post["title"], post["body"])
        used["usedTopics"].append(topic)
        write_json(USED_PATH, used)
        print("발행 완료")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
