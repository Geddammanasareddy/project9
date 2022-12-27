from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def three(request):
    return HttpResponse("<h1><marquee>this is app2 in first view</marquee></h1>")
def four(request):
    return HttpResponse("this is app2 in fourth view")

