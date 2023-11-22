# 프로젝트: 다음 영화 리뷰 수집기
#  - 작성자: ChoLong02
#  - 작성일자: 2023.11.22
#  - 내용: 사용자가 입력해준 영화 코드에 따라 주기별로
#         영화리뷰를 수집하고 MariaDB에 저장하는 프로그램
#  - 기능
#    1. 스케줄러
#    2. 영화 리뷰 수집기(제목, 리뷰, 평점, 작성자, 작성일자)
#    3. DB 저장
#  - 라이브러리: selenium, beautifulsoup4, pymysql, apscheduler

from movie_apple.collector.daum_movie_review import review_collector
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    print("="*100)
    print("== 영화 리뷰 수집기 ver1.0")
    print("="*100)
    movie_code = input("== 영화코드: ")  # 169137
    print('== MSG: "12시간에 한번씩 수집됩니다."')
    scheduler = BlockingScheduler()
    # 매일 12시 0분에 데이터 수집(영화 리뷰)
    scheduler.add_job(review_collector, trigger="cron", args=[movie_code], hour="12", minute="0")
    scheduler.start()


if __name__ == "__main__":
    main()
