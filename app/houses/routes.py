from app.houses import bp
from flask import render_template, redirect, url_for
from app.decorators import login_required
from app.models.houses import listHouses

@bp.route('/houses')
@login_required
def houses():
    return render_template('houses.html')

@bp.route('/houses')
def listHouses():
    return 