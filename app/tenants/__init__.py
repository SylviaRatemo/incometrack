from flask import Blueprint
bp = Blueprint('tenants', __name__)
from app.tenants import routes