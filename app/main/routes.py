from app.main import bp 
from flask import render_template

@bp.route('/')
@bp.route('/login.html')
def index():
    return render_template('login.html')
