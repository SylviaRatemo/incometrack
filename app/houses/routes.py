from app.houses import bp
from flask import render_template, redirect, url_for, session
from app.decorators import login_required
from app.models.houses import Houses
from app.models.user import Users

@bp.route('/houses')
@login_required
def houses():
    email=session.get('email')
    user=Users.query.filter(Users.email == email).with_entities(Users.username).first()
    return render_template('houses.html', houses=Houses.query.all(), user=user, count=Houses.query.count())

@bp.route('/edit')
@login_required
def edit():
    return render_template('edit.html')