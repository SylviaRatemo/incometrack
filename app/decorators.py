from functools import wraps
from flask import session, redirect, url_for, flash

# Custom decorator to check if the user is logged in
def login_required(view_func):
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        if 'username' not in session:
            flash('You must login to view this site.', 'warning')
            return redirect(url_for('login.login'))
        return view_func(*args, **kwargs)
    return decorated_view
