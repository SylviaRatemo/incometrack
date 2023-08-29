from app.houses import bp
from flask import render_template

@bp.route('/houses')
def listHouses():
    return render_template('houses.html')