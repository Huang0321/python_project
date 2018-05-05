from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from stu.models import Student, StudentInfo
from uauth.models import Users

import logging

from rest_framework import mixins, viewsets
from stu.serializers import StudentSerializer
from stu.filters import StuFilter
from rest_framework.response import Response

logger = logging.getLogger('stu')


def index(request):

    if request.method == 'GET':

        # 获取所有学生信息
        stuinfos = StudentInfo.objects.all()
        # num = VisitorStatic.objects.get(id=1).vis_num
        logger.info('Getting studentinfo success')
        return render(request, 'index.html', {'stuinfos': stuinfos})
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
        # if VisitorStatic.objects.get(id=1):
        #     VisitorStatic.objects.get(id=1).vis_num += 1
        # else:
        #     VisitorStatic.objects.create(
        #         vis_num=1
        #     )

        return HttpResponseRedirect('/stu/index/')


def stuPage(request):
    if request.method == 'GET':
        page_id = request.GET.get('page_id', 1)
        stus = Student.objects.all()
        paginator = Paginator(stus, 3)
        page = paginator.page(int(page_id))   # 注意是整型
        return render(request, 'index_page.html', {'stus': page})


class StudentEdit(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    # 查询所有信息
    queryset = Student.objects.all()
    # 序列化
    serializer_class = StudentSerializer

    # 过滤
    filter_class = StuFilter

    # get 到上面的 queryset
    def get_queryset(self):
        # 对结果进行排序
        query = self.queryset
        return query.order_by('-id')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.s_delete = 1
        instance.save()
        return Response({'msg': '删除成功', 'code': 200})


def showStus(request):

    if request.method == 'GET':
        return render(request, 'show.html')


def backStu(request):

    if request.method == 'GET':
        # 过滤语文成绩不及格的学生
        stu1 = Student.objects.filter(s_yuwen__lt=60)
        # 过滤语文成绩大于80 小于90的学生
        stu2 = Student.objects.filter(s_yuwen__lt=90, s_yuwen__gt=80)
        # 过滤状态停级的学生
        stu3 = Student.objects.filter(s_stutaus='NEXT_SCH')
        # 过滤操作时间在 2015年1月1日 至 2018年12月31日的学生
        stu4 = Student.objects.filter(S_operate_time__gt='2015-01-01 00:00:00',
                                      S_operate_time__lt='2018-12-31 59:59:59')
        # 过滤操作时间在2015年1月1日 至 2018年12月31日 语文大于60分 语文小于90分的学生
        stu5 = Student.objects.filter(S_operate_time__gt='2015-01-01 00:00:00',
                                      S_operate_time__lt='2018-12-31 00:00:00',
                                      s_yuwen__gt=60,
                                      s_yuwen__lt=90)

        return render(request, 'back_student.html')