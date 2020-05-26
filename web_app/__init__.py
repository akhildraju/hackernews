# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.models import DB
from web_app.routes.home_routes import home_routes
from web_app.routes.loaddata_routes import loaddata_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(loaddata_routes)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

