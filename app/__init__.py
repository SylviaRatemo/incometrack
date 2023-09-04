from flask import Flask
from app.extensions import db
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import ProgrammingError
import secrets

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except ProgrammingError as e:
            if "Table 'houses' already exists" in str(e):
                print("Table 'houses' already exists. Continuing...")
            else:
                # Handle other programming errors
                print("Error creating database tables:", str(e))
       
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
    print("main works")
    app = create_app()
    app.run()