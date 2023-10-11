import requests
from bs4 import BeautifulSoup
from service.news_service import collect_news
# 다음 뉴스 1 페이지에 내에 있는 모든 기사의 제목, 본문을 수집!
#  → 1건의 기사(제목, 본문)를 수집하기 위해서는 => URL 필요!
#  → 1페이지 내에 있는 모든 기사의 URL 정보를 추출!
#  → 추출 된 URL을 사용해서 daum_news_one.py 코드를 활용하면 완료!

# 1. 1페이지의 URL을 설정
url = "https://news.daum.net/breakingnews/digital"
# 2. 전체소스코드 가져오기
result = requests.get(url)
# 200 code : 성공
# 400~500 code : 실패
# print(result)

# 3. 전체소스코드 → Beautifulsoup4에게 전달
soup = BeautifulSoup(result.text, "html.parser")

# 4. URL 추출
# <ul class="list_news2">
#   <li><a class="link_txt">기사1</a></li>
#   <li><a class="link_txt">기사2</a></li>
#   <li><a class="link_txt">기사3</a></li>
# </ul>
link_list = soup.select("ul.list_news2 a.link_txt")

for i, link in enumerate(link_list):
    new_url = link["href"]
    print("■" * 50)
    print(f"{i+1} URL → {new_url}")
    # 5.new_url을 사용해서 기사(제목+본문)수집 x 15번
    collect_news(new_url)
