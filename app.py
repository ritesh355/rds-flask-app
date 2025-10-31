from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# ✅ Database connection details
db = mysql.connector.connect(
    host="database-1.ckf2cs480fnc.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    user="admin",
    password="password123", #replace with your database password
    database="devopsdb"  #replace with your database name
)

@app.route('/')
def home():
    return "✅ Flask App Connected to AWS RDS!"

@app.route('/users')
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

