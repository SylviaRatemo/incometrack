from flask import Blueprint
bp = Blueprint('login', __name__, url_prefix='/auth')
from app.login import routes