import mysql.connector
from app.models.user import Users

class Login():
	def __init__(self, email, pwd):
		self.email = email
		self.pwd = pwd

	def checkCredentials(self):
		try:
			user = Users.query.filter_by(email=self.email).first()
			#for entry in user:
			#	print(f"Username: {entry.username}, Email: {entry.email}")
			if user and user.password == self.pwd:
				return user.username
			return None
		except Exception as e:
			print(e)
			return None