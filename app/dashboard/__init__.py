from flask import Blueprint
bp = Blueprint('dashboard', __name__)
from app.main import routes