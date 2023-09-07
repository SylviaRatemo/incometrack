from flask import Blueprint
bp = Blueprint('units', __name__)
from app.units import routes