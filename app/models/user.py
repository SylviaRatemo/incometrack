from app.extensions import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
#  Base = declarative_base()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    #engine = create_engine('mysql://root:root@localhost/incometracker')

    #Base.metadata.create_all(engine)

    def __repr__(self):
        return f'<User {self.username}>'