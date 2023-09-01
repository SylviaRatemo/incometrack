from app.login import bp 
from flask import redirect, render_template, jsonify, session, request, url_for
from app.models.login import Login
#from app.houses import bp


@bp.route('/')
@bp.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		_json = request.json
		#print(_json)
		_email = _json['email']
		_password = _json['password']
		
		if _email and _password:
			check = Login(_email, _password)
			user = check.checkCredentials()
			if user != None:
				session['username'] = user
				print("Welcome, " + session.get('username'))
				return jsonify(user)
	return render_template('login.html')

@bp.route('/logout')
def logout():
   session.clear()
   return render_template('login.html')