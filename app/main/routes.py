from app.main import bp 
from flask import render_template, jsonify, session, request

@bp.route('/')
def index():
	return render_template('index.html')