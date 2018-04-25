# -*- coding:utf-8 -*-
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

from stu.models import Student


def addStu(request):

    # 添加学生信息
    if request.method == 'GET':
        return render(request, "index.html")

    if request.method == 'POST':
        # print(request)
        # print(request.POST)

        stu_name = request.POST.get('name')
        stu_sex = 1 if request.POST.get('sex') == '男' else 0
        stu_birth = request.POST.get('birth')
        stu_tel = request.POST.get('tel')

        # 太长
        # stu = Student()
        # stu.stu_name = stu_name
        # stu.stu_birth = stu_birth
        # stu.stu_sex = stu_sex
        # stu.stu_tel = stu_tel
        # stu.save()

        Student.objects.create(
            stu_name=stu_name,
            stu_birth=stu_birth,
            stu_sex=stu_sex,
            stu_tel=stu_tel
        )

        return HttpResponse('添加学生成功')


def selectStu(request):

    # 查询数据
    # stus = Student.objects.all()

    # 查询所有女生
    # stus = Student.objects.filter(stu_sex=False)

    # get
    # stus = Student.objects.get(stu_sex=True)

    # 查询id从大到小的排序
    stus = Student.objects.all().order_by('id')

    # 都返回一条数据，not iterable
        # 获取 id 最大的一条数据
        # stus = Student.objects.all().order_by("id").
        # 获取 id 最小的一条数据
        # stus = Student.objects.all().order_by("id").last

    # 获取男生的数据的个数 stus是一个数
    # stus = Student.objects.filter(stu_sex=True).count()

    # 查询所有80后女生的姓名 filter 里面也可以接很多参数，逗号隔开各个参数
    #stus = Student.objects.filter(stu_sex=False).\
     #   filter(stu_birth__gte='1980-01-01').filter(stu_birth__lte='1989-12-31')


    # 查询姓名以 h 开头 的数据
    # stus = Student.objects.filter(stu_name__startswith='h')
    # 查询姓名以 g 结束 的数据
    # stus = Student.objects.filter(stu_name__endswith='g')
    # 查询 姓名中 包含 u 的数据
    # stus= Student.objects.filter(stu_name__contains='u')

    # 判断是否存在 huang
    # stu = Student.objects.filter(stu_name='huang').exists()
    # print(stu) 可以用在 if 里面

    # 获取指定多个 id 的值
    # ids = [1, 2]
    # stus = Student.objects.filter(id__in=ids)

    # 查询 语文成绩大于数学成绩的学生
    # stus = Student.objects.filter(stu_yuwen__gte=F('stu_shuxue'))

    # 查询 语文成绩超过 数学成绩 10 分的学生
    # stus = Student.objects.filter(stu_yuwen__gte=F('stu_shuxue') + 10)

    # 查询名字不叫 huang 的 或者语文成绩大于70分
    # ~not &and |or
    stus = Student.objects.filter(~Q(stu_name='huang')|Q(stu_yuwen__gt=80))

    # 返回数据给前端
    print(type(stus))
    return render(request, 'sel_stu.html', {'stus': stus})
