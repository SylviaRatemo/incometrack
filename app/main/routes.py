from app.main import bp 
from flask import render_template

@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('index.html')

@bp.route('/profile.html')
def profile():
    return render_template('profile.html')

@bp.route('/login.html')
def login():
    return render_template('login.html')