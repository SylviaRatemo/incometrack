from app.extensions import db
import pymysql
from werkzeug.security import check_password_hash

def login(email, password):
   conn = None;
   cursor = None;

   try:
      conn = db.connect()
      cursor = conn.cursor()

      query = "SELECT email, password FROM users WHERE email=%s"
      query_where = (email,)

      cursor.execute(query, query_where)
      row = cursor.fetchone()

      if row:
         if check_password_hash(row[1], password):
            return row[0]
         return None
   
   except Exception as e:
      print(e)

   finally:
      if cursor and conn:
         cursor.close()
         conn.close()