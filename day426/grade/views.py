from django.shortcuts import render

# Create your views here.
from grade.models import Grades
from stu.models import Students


def show_grades(request):
    gs = Grades.objects.all()

    return render(request, 'all_grades.html', {'gs': gs})


def page_not_found(request):

    return render(request, '404.html')


def server_error(request):

    return render(request, '500.html')


def delStu(request):
    stu_id = request.GET.get('stu_id')
    Students.objects.filter(id=stu_id).delete()

    return Http