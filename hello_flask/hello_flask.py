from flask import Flask

app = Flask(__name__)


# 初始化, __name__代表主模块名称
# 路由是通过装饰器来实现的
@app.route('/')
def hello_world():
    # 视图函数
    return 'Hello World!'


if __name__ == '__main__':
    # 启动项目
    # 运行的项目使用debug模式, 可以调试
    # 并且可以指定端口,主机等
    app.run(debug=True, port='5000', host='0.0.0.0')
