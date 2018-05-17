import os

from flask import Flask

from app.views import blue


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')

    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    app.register_blueprint(blueprint=blue, url_prefix='/hello') # url_prefix 用来区分不同的蓝图

    return app

