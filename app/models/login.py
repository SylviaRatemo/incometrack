import pymysql
from app.extensions import db
from werkzeug.security import check_password_hash

			
def checkCredentials(email, pwd):
	conn = None;
	cursor = None;
	
	try:
		conn = db.connect()
		cursor = conn.cursor()
		
		sql = "SELECT email, password FROM users WHERE email=%s"
		sql_where = (email,)
		
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		
		if row:
			if check_password_hash(row[1], pwd):
				return row[0]
		return None

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()