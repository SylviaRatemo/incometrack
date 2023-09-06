from app.units import bp 
from flask import render_template, jsonify, session, request
from app.decorators import login_required
from app.models.user import Users

@bp.route('/units')
@login_required
def units():
	email=session.get('email')
	user=Users.query.filter(Users.email == email).with_entities(Users.username).first()
	return render_template('units.html', user=user)