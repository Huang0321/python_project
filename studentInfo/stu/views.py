from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
from stu.models import Student


def firPage(request):
    if request.method == 'GET':
        return render(request, 'firstpage.html')

    if request.method == 'POST':
        req = request.POST
        name = req.get('name')
        sex = 1 if req.get('sex') == '男' else 0
        birth = req.get('birth')
        height = req.get('height')

        return HttpResponseRedirect(
            reverse('s:st', kwargs={'name':name, 'sex':sex, 'birth': birth, 'height':height})
        )



def secPage(request, name, sex, birth, height):
    name = name
    sex = sex
    birth = birth
    height = height

    if request.method == 'GET':
        return render(request, 'secondpage.html')

    if request.method == 'POST':
        req = request.POST
        tel = req.get('tel')
        email = req.get('email')
        grade = req.get('grade')
        interest = req.get('interest')

        stu = Student.objects.create(
            stu_name=name,
            stu_sex=sex,
            stu_birth=birth,
            stu_height=height,
            stu_tel=tel,
            stu_email=email,
            stu_grade=grade,
            stu_interest=interest,
        )

        return HttpResponseRedirect(
            reverse('s:info', kwargs={'stu_id': stu.id})
        )


def selStu(request, stu_id):
    stu = Student.objects.filter(id=stu_id).first()

    return render(request, 'stuinfo.html', {'stu':stu})