from app.tenants import bp 
from flask import render_template, jsonify, session, request, sessions
from app.decorators import login_required
from app.models.user import Users

@bp.route('/tenants')
@login_required
def tenants():
	email=session.get('email')
	user=Users.query.filter(Users.email == email).with_entities(Users.username).first()
	return render_template('tenants.html', user=user)