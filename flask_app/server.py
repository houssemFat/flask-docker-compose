from flask import Flask
import mysql.connector
import sys, os, traceback

app = Flask(__name__)


@app.route('/')
def hello(): 
   try :
        user = os.environ["MYSQL_DB_USER"] if "MYSQL_DB_USER" in os.environ else 'flask_app_user'
        database = os.environ["MYSQL_DB_NAME"] if "MYSQL_DB_NAME" in os.environ else 'flask_app_db'
        
        
        password = os.environ["MYSQL_DB_PASSWORD"] if "MYSQL_DB_PASSWORD" in os.environ else 'flask_app_pass'
        host = os.environ["MYSQL_DB_HOST"] if "MYSQL_DB_HOST" in os.environ else '127.0.0.1'
        
        cnx = mysql.connector.connect(user=user, 
                              password=password,
                              host=host,
                              port='3306',
                              database=database)
        cnx.close()
        return "cool"
   except :
        return "Exception {} !".format(sys.exc_info()[0]) 
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
