import secrets

class Config:
    SECRET_KEY = secrets.token_bytes(32)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/incometracker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False