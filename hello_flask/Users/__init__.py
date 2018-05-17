import os

from flask_session import Session
from flask import Flask
import redis

from Users.views import user_app


def create_user_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
    app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
    app.register_blueprint(blueprint=user_app, url_prefix='/user')

    app.config['SECRET_KEY'] = 'secret_key'

    #连接本地
    app.config['SESSION_TYPE'] = 'redis'

    # 连接远程
    # app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='123456')

    # 定义前缀
    app.config['SESSION_KEY_PREFIX'] = 'flask'
    #两种方式 1
    # Session(app)
    # 2
    se = Session()
    se.init_app(app)
    return app


