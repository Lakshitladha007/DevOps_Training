from flask import Flask, request, render_template
import mysql.connector
import time
import os

app = Flask(__name__)

# Retry DB connection
while True:
    try:
        db = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "mysql-db"),
            user=os.environ.get("DB_USER", "user"),
            password=os.environ.get("DB_PASSWORD", "pass"),
            database=os.environ.get("DB_NAME", "mydb")
        )
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS entries (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100));")
        db.commit()
        break
    except Exception as e:
        print("Waiting for DB...", e)
        time.sleep(3)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("INSERT INTO entries (name) VALUES (%s);", (name,))
        db.commit()
    cursor.execute("SELECT * FROM entries;")
    rows = cursor.fetchall()
    return render_template('index.html', entries=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
