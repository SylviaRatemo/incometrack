from app.extensions import db

class Houses(db.Model):
    houseId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    unitCount = db.Column(db.Integer, nullable=False)
    occupancyRate = db.Column(db.Integer)
    totalRent = db.Column(db.Numeric(10,2), nullable=False)
    
    def __init__(self, houseId, name, location, unitCount, occupancyRate, totalRent):
        self.houseId = houseId
        self.name = name
        self.location = location
        self.unitCount = unitCount
        self.occupancyRate = occupancyRate
        self.totalRent = totalRent