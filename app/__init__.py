from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)