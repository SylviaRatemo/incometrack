from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Units(db.Model):
    unitId = db.Column(db.Integer, primary_key=True)
    houseId = db.Column(db.Integer, ForeignKey('house.houseId'), primary_key=True)
    tenantId = db.Column(db.Integer, nullable=False)
    meterNo = db.Column(db.Integer)
    description = db.Column(db.Text)
    status = db.Column(db.Bool)
    rentId = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.name}'