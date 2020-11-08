from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
    return HttpResponse('叫我登录')