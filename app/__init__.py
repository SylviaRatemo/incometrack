from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'admin'
    # app.config['MYSQL_PASSWORD'] = 'admin'
    # app.config['MYSQL_DB'] = 'incometrack'

    db.init_app(app)

    # db = SQLAlchemy(app)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.login import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    return app