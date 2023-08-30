from app.houses import bp
from flask import render_template, redirect, url_for

@bp.route('/houses')
def index():
    return render_template('houses.html')