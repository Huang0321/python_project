
import random
import time

from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

from uauth.models import Users
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# Create your views here.


def regist(request):

    if request.method == 'GET':

        return render(request, 'day6_regist.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        password = make_password(password)
        Users.objects.create(
            u_name=name,
            u_password=password
        )
        return HttpResponseRedirect('/uauth/login/')


def login(request):

    if request.method == 'GET':

        return render(request, 'day6_login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中， set_cookie(key, value, seconds)
        name = request.POST.get('name')
        password = request.POST.get('password')

        if Users.objects.filter(u_name=name).exists():
            user = Users.objects.get(u_name=name)
            if check_password(password, user.u_password):
                s = 'abcdefghijklmnopqrstuvwxyz1234567890'
                ticket = ''
                for i in range(15):
                    # 获取随机字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket += 'TK_' + ticket + str(now_time)
                # ticket = 'abcdefg'
                # 绑定令牌到cookie里面
                # response = HttpResponse('登录成功')
                response = HttpResponseRedirect('/stu/index/')
                response.set_cookie('ticket', ticket, max_age=10000)
                # 存在服务端
                user.u_ticket = ticket
                user.save()
                return response
            else:
                return render(request, 'day6_login.html', {'password': '密码不正确'})

        else:
            return render(request, 'day6_login.html', {'name': '用户不存在'})


def logout(request):

    if request.method == 'GET':
        response = HttpResponse('/uauth/login/')
        response.delete_cookie('ticket')
        return response


def djlogin(request):

    if request.method == 'GET':

        return render(request, 'login.html')

    if request.method == 'POST':

        name = request.POST.get('name')
        password = request.POST.get('password')

        # 验证用户名和密码, 通过的话，返回user对象
        user = auth.authenticate(username=name, password=password)

        if user:
            # 验证成功，登录
            auth.login(request, user)
            return HttpResponseRedirect('/stu/index/')
        else:
            return render(request, 'index.html')


def djregist(request):

    if request.method == 'GET':
        return render(request, 'day6_regist.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        User.objects.create_user(username=name, password=password)
        return HttpResponseRedirect('/uauth/dj_login/')


def djlogout(request):

    if request.method == 'GET':

        auth.logout(request)
        return HttpResponseRedirect('/uauth/djlogin/')



