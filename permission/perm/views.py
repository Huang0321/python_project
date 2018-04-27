from django.shortcuts import render
from perm.models import User, Permission, Role

# Create your views here.


def addUser(request):
    if request.method == 'get':
        if request.method == 'post':
            name = request.POST.get('name')
            sex = 1 if request.POST.get('sex') == 'male' else 0
            birth = request.POST.get('birth')
            r_id = request.POST.get('r_id')

            User.objects.create(
                u_name=name,
                u_sex=sex,
                u_birth=birth,
                role=r_id
            )

        return render(request, 'adduser.html')


def selPerm(request):

    if request == 'GET':
        pass

    return render(request, 'selperm.html')