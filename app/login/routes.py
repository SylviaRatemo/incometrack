from app.login import bp 
from app.extensions import db
from app.models.login import login
from flask import jsonify, request, session
import json


@bp.route('/')
@bp.route('/login.html', methods=['GET', 'POST'])
def login():
    print(request.data.decode('utf-8'))
    if request.method == 'POST':
        try:
            print("Step 2 pass")
            _json = request.get_json()
            print(_json)
            _email = _json.get('email')
            _password = _json.get('password')

            print("Step 3 pass")
            if _email and _password:
                user = login(_email, _password)

                if user != None:
                    session['email'] = user
                    return jsonify({'message' : 'Successful login!'})
            
            response = jsonify({'message' : 'Bad Request - Invalid credentials!'})
            response.status_code = 400
            return response
        except Exception as e:
            print("Error parsing JSON:", e)
            response = jsonify({'message' : 'Error parsing JSON data!'})
            response.status_code = 400
            return response