from flask import Flask, render_template
# import sys
from flask_script import Manager

# args = sys.argv
# args1 = args[1]
# args2 = args[2]

app = Flask(__name__)
manager = Manager(app=app)


@app.route('/hello/<name>/<int:sb>/')
def first_flask(name, sb):
    print(type(name))
    print(type(sb))
    return 'hello' + name + str(sb)


@app.route('/index/')
def hello_flask():
    return render_template('hello_flask.html')


if __name__ == '__main__':
    # app.run(debug=True, port='5050', host='0.0.0.0')
    manager.run()
