# K-Market-Project

Flask로 구축한 웹 애플리케이션으로, 웹 서버를 통해 클라이언트와 상호작용하고 데이터를 처리하는 구조

This project includes a simple Flask API (`API sample.py`) that interacts with a SQLite database (`sample.db`).

## Prerequisites

To run this project, you will need the following installed on your machine:

- Python 3.x
- `pip` (Python package installer)
- SQLite3
1. pip install Flask
2. sudo apt update
3. sudo apt install sqlite3
   
## How to access SQLite3

1. sqlite3 sample.db                                 # 
2. .tables                                           # 데이터 베이스 내 테이블 확인
3. PRAGMA table_info(customers);                     # 테이블 구조 확인
4. SELECT * FROM customers;                          # 특정 데이터 조회 (in this case, customers)
5. SELECT * FROM customers WHERE City = 'New York';  # 데이터 필터링 및 조회 ex) City가 New York인 고객만 조회
6. .exit  or .quit                                   # SQLite 종료

## Setup

1. **Clone the repository**:
   First, clone this repository to your local machine using the following command:

   git clone https://github.com/Sheon0109/K-Market-Project.git


  cd K-Market-Project
   
## Run
python 'API sample.py'

Flask 서버 실행 되면, 브라우저로 url 복사 해서  API 엔드포인트 접근

Main Page: http://127.0.0.1:5000/
About Page: http://127.0.0.1:5000/about
Customers Data: http://127.0.0.1:5000/customers


