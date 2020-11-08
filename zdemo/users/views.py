from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def register(request):
    return HttpResponse('注册接口')


def index(request):
    return HttpResponse('hello world Django!')
def a(request):
    return HttpResponse('1!')
def b(request):
    return HttpResponse('2!')