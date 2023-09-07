from flask import Blueprint
bp = Blueprint('houses', __name__)
from app.houses import routes