from app.login import bp 
from flask import redirect, render_template, jsonify, session, request
from app.models.login import checkCredentials

@bp.route('/', methods=['GET', 'POST'])
def login():
	_json = request.json
	#print(_json)
	_email = _json['email']
	_password = _json['password']
	
	if _email and _password:
		user = checkCredentials(_email, _password)
		if user != None:
			session['email'] = user
			return redirect('/houses')

	resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
	resp.status_code = 400
	return resp 