# Web Crawler
#  1.기본(requests + bs4)
#  2.심화(requests + selenium)

# requests는 현재 URL의 정적인 페이지 소스코드만 수집 가능
#  → 더보기 등 버튼을 눌러야 나오는 동적인 정보는 수집 불가

# selenium은 URL의 정적, 동적 소스코드 모두 수집 가능
#  → 자기자신만의 브라우저를 사용해서 동작하기 때문에 모두 수집 가능
#  → 따라서, chromedriver와 같은 브라우저 설정 반드시 필요!

# pip install beautifulsoup4
# pip install selenium
# pip install webdriver_manager


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1.Selenium을 위한 ChromDriver 설치
#   1-1.직접 다운로드
#     - https://sites.google.com/chromium.org/driver/
#   1-2.실시간 다운로드 후 사용
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)







