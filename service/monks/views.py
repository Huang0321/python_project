from django.http import HttpResponse
from django.shortcuts import render
from monks.models import Monks

# Create your views here.


def add_monk(request):

    print(request)

    if request.method == "GET":
        return render(request, "monk_list.html")

    if request.method == "POST":

        monk_name = request.POST.get('name')
        monk_sex = 1 if request.POST.get('sex') == '男' else 0
        monk_birth = request.POST.get('birth')
        monk_tel = request.POST.get('tel')

        Monks.objects.create(
            monk_name=monk_name,
            monk_sex=monk_sex,
            monk_birth=monk_birth,
            monk_tel=monk_tel
        )

        return HttpResponse("注册成功")


def select_monk(request):

    monks = Monks.objects.all()

    return render(request, 'select_monk.html', {'monks': monks})