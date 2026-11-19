#!/usr/bin/env python3
"""빙(IndexNow)에 바뀐 페이지 주소를 알립니다.
사용법:
  python3 scripts/indexnow.py --all            사이트맵의 모든 주소
  python3 scripts/indexnow.py 파일1.html ...   바뀐 파일만
"""
import json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(ROOT, "scripts", "indexnow.json")))
HOST, KEY = cfg["host"], cfg["key"]
SKIP = ("ad/", "ig/", "scripts/", ".github/", "node_modules/")

def sitemap_urls():
    s = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", s)

def file_to_url(path):
    path = path.strip().lstrip("./")
    if not path.endswith(".html") or path.startswith(SKIP) or path.endswith("404.html"):
        return None
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return None  # 지운 파일은 알리지 않음
    head = open(full, encoding="utf-8", errors="ignore").read(6000)
    if re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', head, re.I):
        return None  # 검색에 안 띄우는 페이지
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', head, re.I)
    if m and m.group(1).startswith("https://" + HOST):
        return m.group(1)  # 대표 주소가 있으면 그 주소로
    rel = path[:-len("index.html")] if path.endswith("index.html") else path
    return "https://%s/%s" % (HOST, urllib.parse.quote(rel))

def main(args):
    if not args:
        print("알릴 파일 없음"); return
    if args == ["--all"]:
        urls = sitemap_urls()
    else:
        urls = [u for u in (file_to_url(a) for a in args) if u]
    urls = [u for u in dict.fromkeys(urls) if urllib.parse.urlparse(u).hostname == HOST]
    if not urls:
        print("알릴 주소 없음"); return
    body = json.dumps({"host": HOST, "key": KEY,
                       "keyLocation": "https://%s/%s.txt" % (HOST, KEY),
                       "urlList": urls[:10000]}).encode()
    for attempt in range(3):
        try:
            req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                headers={"Content-Type": "application/json; charset=utf-8"})
            with urllib.request.urlopen(req, timeout=30) as r:
                print("IndexNow 응답 %s, 주소 %d개" % (r.status, len(urls)))
                for u in urls[:20]: print("  ", u)
                return
        except urllib.error.HTTPError as e:
            print("IndexNow 오류 %s: %s" % (e.code, e.read()[:300]))
            if e.code in (400, 403, 422): break  # 고쳐야 하는 오류는 재시도 안 함
        except Exception as e:
            print("연결 실패:", e)
        time.sleep(20)
    # 알림 실패해도 사이트 배포에는 영향 없도록 성공으로 끝냄

if __name__ == "__main__":
    main(sys.argv[1:])
