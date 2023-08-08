from flask import Flask
from config import Config
from app.extensions import db
from flask_mysqldb import MySQL
import secrets

def create_app(config_class=Config):
    app = Flask(__name__)
    # JSON error
    app.config['JSON_AS_ASCII'] = False

    app.secret_key = secrets.token_bytes(32)

    app.config.from_object(config_class)

    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    app.config['MYSQL_DATABASE_USER'] = 'admin'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
    app.config['MYSQL_DATABASE_DB'] = 'incometrack'

    db.init_app(app)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.login import bp as login_bp
    app.register_blueprint(login_bp)
    
    return app