from app.dashboard import bp 
from flask import render_template, jsonify, session, request
from app.decorators import login_required
from app.models.user import Users

@bp.route('/dashboard')
@login_required
def dash():
	email=session.get('email')
	user=Users.query.filter(Users.email == email).with_entities(Users.username).first()
	return render_template('index.html', user=user)