
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from student.views import stu


def create_app():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')

    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask2'

    app.register_blueprint(blueprint=stu, url_prefix='/stu')

    SQLAlchemy(app=app)

    return app
