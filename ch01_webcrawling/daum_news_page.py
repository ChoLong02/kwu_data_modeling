# 다음뉴스 1 page -> 15 news
#  - 페이지를 돌면서 수집 => 끝날때까지
import requests
from bs4 import BeautifulSoup
from service.news_service import collect_news

page = 1
count = 0
while True:
    print(f"{page}page" + "▲" * 50)
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    link_list = soup.select("ul.list_news2 a.link_txt")
    if len(link_list) == 0:
        break
    for i, link in enumerate(link_list):
        new_url = link["href"]
        print("■" * 50)
        print(f"{i + 1} URL → {new_url}")
        collect_news(new_url)
        count += 1
    page += 1

print(f"**DAUM NEWS 수집기**")
print(f"총 {page-1} page, {count}건의 NEWS가 수집되었습니다.")
