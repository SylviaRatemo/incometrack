import mysql.connector
from app.models.user import Users
from werkzeug.security import check_password_hash


def checkCredentials(email, pwd):
	try:
		user = Users.query.filter_by(email=email).first()
		#for entry in user:
		#	print(f"Username: {entry.username}, Email: {entry.email}")
		if user and user.password == pwd:
			return user.email
		return None
	except Exception as e:
		print(e)
		return None