from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from stu.models import Student, StudentInfo, VisitorStatic
from uauth.models import Users



def index(request):

    if request.method == 'GET':

        # 获取所有学生信息
        stuinfos = StudentInfo.objects.all()
        num = VisitorStatic.objects.get(id=1).vis_num
        return render(request, 'index.html', {'stuinfos': stuinfos, 'num': num})
        # else:ticket = request.COOKIES.get('ticket')
        # if not ticket:
        #     return HttpResponseRedirect('/uauth/login/')
        # if Users.objects.filter(u_ticket=ticket).exists():
        # HttpResponseRedirect('/uauth/login/')


def addStu(request):

    if request.method == 'GET':

        return render(request, 'addStu.html')

    if request.method == 'POST':
        #
        name = request.POST.get('name')
        tel = request.POST.get('tel')

        stu = Student.objects.create(
            s_name=name,
            s_tel=tel
        )

        return HttpResponseRedirect(
            reverse("s:info", kwargs={'stu_id': stu.id})
        )


def addStuInfo(request, stu_id):

    if request.method == 'GET':

        return render(request, 'addStuinfo.html', {'stu_id':stu_id})

    if request.method == 'POST':

        stu_id = request.POST.get('stu_id')
        addr = request.POST.get('addr')

        # 获取头像图片
        img = request.FILES.get('img')

        StudentInfo.objects.create(
            s_id=stu_id,
            i_addr=addr,
            i_unage=img,
        )
        if VisitorStatic.objects.get(id=1):
            VisitorStatic.objects.get(id=1).vis_num += 1
        else:
            VisitorStatic.objects.create(
                vis_num=1
            )

        return HttpResponseRedirect('/stu/index/')


def stuPage(request):
    if request.method == 'GET':
        page_id = request.GET.get('page_id', 1)
        stus = Student.objects.all()
        paginator = Paginator(stus, 3)
        page = paginator.page(int(page_id))   # 注意是整型
        return render(request, 'index_page.html', {'stus': page})