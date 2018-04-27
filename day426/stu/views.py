from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from stu.models import Students

def show_students(request, g_id):
    # request.GET 是一个字典
    # g_id = request.GET.get('g_id')
    # stus = Students.objects.filter(g_id=g_id)

# stus = Students.objects.filter(g_id=g_id)
#
    # return render(request, 'show_students.html', {'stus': stus})
    return HttpResponseRedirect(
        reverse('s:restu', kwargs={'g_id': g_id})
        )

def redirectStu(request, g_id):
    stus = Students.objects.filter(g_id=g_id)

    return render(request, 'show_students.html', {'stus': stus})


def selStu(request, m, n, p):

    return HttpResponse('获取url参数的多种方法')

#
# def selStu(request, month, day, year):
#
#     return HttpResponse('获取url参数的多种方法')

# Students.objects.update(s_name='sb') 或 查到名字之后 给名字赋值 再调用 save()方法