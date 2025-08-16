from flask import Flask
from database.conection import create_tables

def create_app():
    app = Flask(__name__)
    create_tables()

    from app.views import bp
    app.register_blueprint(bp)

    return app
