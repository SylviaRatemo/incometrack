from flask import Flask
from app.extensions import db
from config import Config
from flaskext.mysql import MySQL
import secrets

def create_app(config_class=Config):
    app = Flask(__name__)

    app.secret_key = secrets.token_bytes(32)

    app.config.from_object(config_class)

    db.init_app(app)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.login import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    return app