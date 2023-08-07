import os

basedir = os.path.abspath(os.path.dirname(__file__))

db_config = {
        'host': 'localhost',
        'user': 'admin',
        'password': 'admin',
        'database': 'incometrack'
   }

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql://admin:admin@localhost:5000/incometrack'
    SQLALCHEMY_TRACK_MODIFICATIONS = False