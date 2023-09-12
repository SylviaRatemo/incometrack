from app.houses import bp
from flask import render_template, redirect, url_for, session, request
from app.decorators import login_required
from app.models.houses import Houses
from app.models.user import Users

@bp.route('/houses')
@login_required
def houses():
    email=session.get('email')
    user=Users.query.filter(Users.email == email).with_entities(Users.username).first()
    return render_template('houses.html', houses=Houses.query.all(), user=user, count=Houses.query.count(), id=id)

@bp.route('/edit', methods=['POST', 'GET'])
@login_required
def edit():
    email=session.get('email')
    user=Users.query.filter(Users.email == email).with_entities(Users.username).first()
    id = request.form.get('house_id')
    print(id)
    house = Houses.query.get(id)
    # edit the house
    if request.method == 'POST' :
        _json = request.get_json()
        if house:
            #name = _json.get('name', house.name)
            #location = _json.get('location', house.location)
            house.edit(_json['name'],
                       _json['location'],
                        _json['unitcount'],
                        _json['occupancyrate'],
                        _json['totalrent'])
            print("Submitted")
            return redirect(url_for('houses.houses'))
        else:
            return 'No house with that id'
    else:
        return render_template('edit.html', user=user, house=house)