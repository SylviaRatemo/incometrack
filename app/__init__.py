from flask import Flask
from app.extensions import db
from config import Config
from flask_sqlalchemy import SQLAlchemy
import secrets

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    db.init_app(app)    
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.login import bp as login_bp
    app.register_blueprint(login_bp)
    
    from app.houses import bp as houses_bp
    app.register_blueprint(houses_bp)

    from app.units import bp as units_bp
    app.register_blueprint(units_bp)

    from app.tenants import bp as tenants_bp
    app.register_blueprint(tenants_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)