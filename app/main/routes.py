from app.main import bp 
from flask import render_template, jsonify, session, request
from app.decorators import login_required

@bp.route('/dashboard')
@login_required
def index():
	return render_template('index.html')