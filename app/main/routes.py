from app.main import bp 
from flask import render_template, jsonify, session, request

@bp.route('/')
@bp.route('/login')
def units():
	return render_template('login.html')