from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home1(request):
    return HttpResponse("this is home1 from app1")


def home2(request):
    return HttpResponse("<b> this is home2 from app1<b>")


def home3(request):
    return HttpResponse("<i>This is home3 from app1<i>")
