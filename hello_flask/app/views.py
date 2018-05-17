# 主要是用来处理业务逻辑
import uuid

from flask import Blueprint, send_file, render_template, request, make_response, redirect, url_for, abort

# blue = Blueprint('first', __name__, template_folder='../templates')
blue = Blueprint('first', __name__)


@blue.route('/')
def hello_world():
    # 视图函数
    return render_template('hello_flask.html')


@blue.route('/index/')
def index():
    return send_file('../templates/hello_flask.html')


@blue.route('/getfloat/<float:price>/')
def hello_float(price):

    return 'float %f' % price


@blue.route('/getstr/<string:name>/')
def hello_name(name):
    return 'hello %s' % name


# path: 获取url中的路径， '/' 也当做字符串返回
@blue.route('/getpath/<path:url_path>/', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def hello_path(url_path):

    return 'path: %s' % url_path


@blue.route('/getuuid/')
def hello_uuid():
    a = uuid.uuid4()
    return str(a)


@blue.route('/getbyuuid/<uuid:uu>/')
def get_uuid(uu):
    return 'uu: %s' % uu


@blue.route('/getrequest/', methods=['GET', 'POST'])
def get_request():
    a = request
    args = a.args
    form = a.form
    print(args)
    print(form)

    return '获取requst'


@blue.route('/makeresponse/')
def responses():
    response = make_response('<h2>呵呵哒<h2>')

    return response, 200


@blue.route('/redirect/')
def redirects():
    # 第一种方法
    # return redirects('/hello/index/')
    # 第二种方法
    return redirect(url_for('first.index'))


@blue.route('/makeabort/')
def make_abort():
    abort(404)
    return '终结'


@blue.errorhandler(404)
def get_error(exception):

    return '捕捉异常:%s' % exception