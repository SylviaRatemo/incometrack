import mysql.connector
from app import db
from werkzeug.security import check_password_hash

			
def checkCredentials(email, pwd):
	conn = None;
	cursor = None;
	
	try:
		conn = db.connect()
		if conn:
			print("conn")
			
		cursor = conn.cursor()
		
		sql = "SELECT email, password FROM users WHERE email=%s"
		
		sql_where = (email,)
		
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		
		if row:
			if check_password_hash(row[1], pwd):
				#return row[0]
				print(row[0])
				return True
		return None

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()