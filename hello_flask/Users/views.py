import random
from datetime import datetime

from flask import Blueprint, render_template, request, session, redirect, url_for, make_response

user_app = Blueprint('second', __name__)


@user_app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = session.get('username')
        return render_template('login.html', username=username)
    else:
        username = request.form.get('username')
        session['username'] = username

        return redirect(url_for('second.login'))


@user_app.route('/getresponse/')
def get_response():

    response = make_response('<h2>呵呵哒</h2>', 200) # 添加状态码, 也可以在return 加
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ticket = ''
    for _ in range(20):
        ticket += random.choice(letters)

    response.set_cookie('ticket', ticket, max_ages=500, expire='')

    return response


@user_app.route('/deletecookie/')
def del_cookie():

    respose = make_response('<h2>呵呵</h2>')
    respose.delete_cookie('ticket')

    return respose