from flask import Flask
from app.extensions import db
from config import Config


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(str(e))
    
from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app.dashboard import bp as dash_bp
app.register_blueprint(dash_bp)

from app.login import bp as login_bp
app.register_blueprint(login_bp)

from app.houses import bp as houses_bp
app.register_blueprint(houses_bp)

from app.units import bp as units_bp
app.register_blueprint(units_bp)

from app.tenants import bp as tenants_bp
app.register_blueprint(tenants_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)