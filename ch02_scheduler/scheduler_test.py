# 스케줄러
#  - 일정 시간에 반복적으로 작업
#  - 12시간에 한번씩~
#  - 5분에 한번씩~
#  - 스케줄러 + 데이터 수집

#  - CRON 표기법(스케줄러 날짜)
import time
from apscheduler.schedulers.background import BackgroundScheduler

# 스케줄러 생성!
sched = BackgroundScheduler()
# 스케줄러에게 임무 부여하기
def print_hello():
    print("Hello")

# trigger
#  1.date: 특정 날짜 및 시간에 1번만 동작
#  2.CRON: 만능(주로 하루에 특정시간에)
#  3.interval: 주기별로(5초, 10분, 1시간 → 1번씩)
# sched.add_job(print_hello, "interval", seconds=5, id="kwu")
sched.add_job(print_hello, "cron", hour='12', minute='7', id="kwu")
sched.start()

# backgroundscheduler -> 어떤 동작 뒤에서 묵묵히 작업
while True:
    time.sleep(1)