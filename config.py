import os
import mysql.connector

basedir = os.path.abspath(os.path.dirname(__file__))

db_config = {
        'host': 'localhost',
        'user': 'admin',
        'password': 'admin',
        'database': 'incometrack'
    }

class Config:
    try:
        connection = mysql.connector.connect(**db_config)
        connection.close()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))


