from flask import Flask, request
import mysql.connector
import socket

app = Flask(__name__)
config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'trivago'
    }
connection = mysql.connector.connect(**config)

@app.route('/') 
def hello():
    sql_insert_query = "INSERT INTO table_name VALUES (NULL, 'my name')"
    cursor = connection.cursor()
    result  = cursor.execute(sql_insert_query)
    connection.commit()
    
    count = redis.incr('hits')
    return 'Hey! This is : {} , I have been seen in the database {} times.\n'.format(socket.gethostbyname(socket.gethostname()), count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)