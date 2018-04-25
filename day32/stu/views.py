from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from grade.models import Grade

# Create your views here.
from stu.models import Student, StudentInfo, GoodsUser, Goods


def addStu(request):
    if request.method == 'GET':
        return render(request, 'addstu.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        birth = request.POST.get('birth')
        stu_yuwen = request.POST.get('yuwen')
        stu_shuxue = request.POST.get('shuxue')
        Student.objects.create(
            stu_name=name,
            stu_sex=1 if sex == '男' else 0,
            stu_birth=birth,
            stu_yuwen=stu_yuwen,
            stu_shuxue=stu_shuxue
        )

        return render(request, 'addstu.html')


def selStu(request):

    # 通过扩展表学生的地址去查找学生的信息
    #  查找 成都锦江区 的学生信息

    # stus = StudentInfo.objects.filter(stu_addr='成都锦江区')
    # stu = stus[0]
    # selstu = Student.objects.filter(id=stu.id)

    # 通过 知道学生的地址来找学生的姓名
    # stus = StudentInfo.objects.filter(stu_addr__contains='成都锦江区')
    # stu = stus[0]
    # selstu = stu.stust

    st = Student.objects.filter(stu_name='达叔')
    stu = st.first()
    # selstu = StudentInfo.objects.filter(stu_id=stu.id).first()
    # 第一种 方法
    # selstu = stu.StudenInfo.objects
    # 第二种 方法 关联
    selstu = stu.stu_info



    return render(request, 'selstu.html', {'selstu':selstu})


def fselStu(request):

    # 查询 Python 班级的学生
    # 方法 1
    # g = Grade.objects.get(g_name='python')
    # stus = Student.objects.filter(g_id=g.id)
    # 方法 2
    # g = Grade.objects.get(g_name='python')
    # stus = g.student_set.all()

    # 查询名叫 李空空的班级
    # stu = Student.objects.get(stu_name='李空空')
    # gs = stu.g

    # 查询 html班下 成绩大于90分的信息
    g = Grade.objects.get(g_name='html')
    stus = g.student_set.filter(stu_yuwen__gte=90)

    # 查询 html 中出生在 80后中的男生的信息
    g = Grade.objects.get(g_name='html')
    stus = g.student_set.filter(stu_birth__gte='1980-1-1', stu_sex=0)

    # 查询 html 班级下 语文成绩查过数学成绩10分的男同学的信息
    g = Grade.objects.get(g_name='html')
    stus = g.student_set.filter(stu_yuwen__gte=F('stu_shuxue') + 10)

    return render(request, 'selgrade.html', {'stus': stus})


def manyGoods(request):

    # 获取小乔购买的商品
    u = GoodsUser.objects.filter(u_name='小乔')[0]
    goods = u.goods_set.all()

    # 获取购买娃哈哈用户的信息
    g = Goods.objects.filter(g_name='娃哈哈')[0]
    users = g.g_user.all()

    return render(request, 'good.html', {'goods': goods, 'users': users})


def allStu(request):

    stus = Student.objects.all()
    return render(request, 'all_stus.html', {'stus':stus})