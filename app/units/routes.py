from app.units import bp 
from flask import render_template, jsonify, session, request
from app.decorators import login_required

@bp.route('/units')
@login_required
def units():
	return render_template('units.html')