from flask import Flask, request
from flaskext.mysql import MySQL
import socket

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'trivago'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
mysql.init_app(app)

@app.route('/') 
def hello():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE first_name LIKE '%Mario%';")
    data = cursor.fetchone()
    return 'Hey! This is : {} , This a website for customer {}\n'.format(socket.gethostbyname(socket.gethostname()), data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)