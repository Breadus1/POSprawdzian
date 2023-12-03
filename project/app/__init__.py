from flask import Flask

def create_app():
    app = Flask(__name__)

    from .users import users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    return app
