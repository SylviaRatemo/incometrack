from app.tenants import bp 
from flask import render_template, jsonify, session, request
from app.decorators import login_required

@bp.route('/tenants')
@login_required
def tenants():
	return render_template('tenants.html')