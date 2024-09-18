from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# 데이터베이스 파일 경로 설정
DATABASE = '/mnt/c/Users/ksch3/Downloads/chinook.db'

# 데이터베이스 연결 함수
def connect_db():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# 기본 페이지
@app.route('/')
def index():
    return "Welcome to the API"

# About 페이지
@app.route('/about')
def about():
    return "This is a sample API built with Flask"

# customers 정보 조회 API
@app.route('/customers', methods=['GET'])
def get_customers():
    conn = connect_db()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM customers')  # customers 테이블에서 모든 데이터 조회
        data = cursor.fetchall()
        conn.close()

        # 데이터를 JSON 형식으로 반환
        customer_list = [
            {
                'CustomerId': row[0],
                'FirstName': row[1],
                'LastName': row[2],
                'Company': row[3],
                'Address': row[4],
                'City': row[5],
                'State': row[6],
                'Country': row[7],
                'PostalCode': row[8],
                'Phone': row[9],
                'Email': row[11]
            } for row in data
        ]
        return jsonify(customer_list)
    except sqlite3.Error as e:
        print(f"SQL query error: {e}")
        return jsonify({"error": "Failed to retrieve data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
