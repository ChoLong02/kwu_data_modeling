import requests
from bs4 import BeautifulSoup


# 기능(함수) 1. daum news에서 기사(제목+본문) 수집기
#   - 입력(parameter): url
#   - 출력: 기사(제목+본문)
def collect_news(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    print(f"제목: {title}")
    contents = doc.select("section > p")
    content = ""
    for i, p in enumerate(contents):
        content = content + p.get_text()
    print(f"본문: {content}")