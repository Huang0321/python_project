from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def hello(request):
    return HttpResponse('hello world')


def show(request):
    return HttpResponse('show your face')