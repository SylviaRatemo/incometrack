from app.main import bp 
from flask import render_template

@bp.route('/login')
def index():
    return render_template('login.html')