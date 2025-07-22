from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)
    return app, api

api, app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

    

