from app.extensions import db

class Houses(db.Model):
    houseId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    unitCount = db.Column(db.Integer, nullable=False)
    occupancyRate = db.Column(db.Bool)
    rentId = db.Column(db.Integer)
    totalRent = db.Column(db.Numeric(10,2), nullable=False)

    def __init__(self, houseId):
        self.houseId = houseId
    
    def listHouses():
        try:
            #houseDict = {}
            houses = Houses.query.all()
            for entry in houses:
                #houseDict['entry.houseId'] = entry.name
                return entry
            return None
        except Exception as e:
            print(e)
            return None

    def __repr__(self):
        return f'{self.name}'