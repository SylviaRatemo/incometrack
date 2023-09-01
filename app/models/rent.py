from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Rent(db.Model):
    rentId = db.Column(db.Integer, primary_key=True)
    unitId = db.Column(db.String(30), ForeignKey('rent.rentId'))
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Bool)
    rentId = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.name}'