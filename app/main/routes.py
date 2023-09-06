from app.main import bp 
from flask import render_template


@bp.route('/about')
@bp.route('/')
def index():
	return render_template('about.html')