from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Tenants(db.Model):
    tenantId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    IdNumber = db.Column(db.Integer, nullable=False)
    unitId = db.Column(db.String(30), ForeignKey('unit.unitId'))
    rentId = db.Column(db.Integer, ForeignKey('rent.rentId'))

    def __repr__(self):
        return f'{self.name}'