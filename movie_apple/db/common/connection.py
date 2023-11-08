# **DBMS(데이터베이스 관리 시스템) 소개
#  - 데이터를 저장하고 관리(중복, 관계, 기타 등등)

# **DBMS 종류
#  1.RDB(관계형 데이터베이스) - 전통적인(스키마:명세서)
#    - ORACLE
#    - MySQL
#    - MariaDB
#  2.NoSQL - New
#    - MongoDB
#    - Redis

# ** Pycharm과 DB 동작 과정
#  - Pycharm은 통합개발환경도구 → 모든 개발은 여기서!
#
#  1.Pycharm  →  Connection정보  →  MariaDB
#              (IP, PORT, ID, PW)
# IP: 컴퓨터 접속 주소(ex: 210.112.35.52)
# PORT: 컴퓨터 내에 설치 된 프로그램의 위치(ex: 3306)
# IP+PORT: 210.112.35.52:3306

# 2.Pycharm  →  SQL  →  MariaDB
#  - SQL(구조질의어): RDB를 사용하기위해서는 반드시 필요!
#  - 대부분 SQL로 CRUD 작업 진행
#  - Create: 입력 → INSERT
#  - Read  : 조회 → SELECT
#  - Update: 수정 → UPDATE
#  - Delete: 삭제 → DELETE

import pymysql

# DB 연결
def conn():
    conn = pymysql.connect(
        host="127.0.0.1",  # IP
        port=3306,
        user="root",       # ID(root:최고관리자)
        password="1234",   # PW
        db="",
        charset="utf8",
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )

