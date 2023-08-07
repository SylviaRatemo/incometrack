from app.login import bp 
from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb.cursors
import re
from app.extensions import db
from app.models.login import Login

@bp.route('/login.html', methods = ('GET', 'POST'))
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND email = %s', (username, email))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Login Success!'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Wrong credentials!'
    return render_template('login.html', msg = msg)

@bp.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))