import mysql.connector
from password import dbpassword

def connectTo(hostname, username, password, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            passwd = password,
            database = dbname
        )
        print("Connected to MySQL Database: " + dbname)
    except Exception as err:
        print(err)

    return connection

connection = connectTo("localhost", "root", f"{dbpassword}", "library")

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(err)
    
def readQuery(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(err)

        