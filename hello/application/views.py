from django.shortcuts import render
from django.http import HttpResponse
from application.models import Student

# Create your views here.
def show(request):
    return HttpResponse('show your face')

def addStudent(request):
    print(request)
    stu = Student()
    stu.name = '张三'
    stu.sex = 1

    stu.save()

    return HttpResponse('添加成功')
