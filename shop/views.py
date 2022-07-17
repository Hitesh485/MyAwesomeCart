from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("We are at about page")


def contact(request):
    return HttpResponse("We are at contact page")


def tracker(request):
    return HttpResponse("We are at tracker page")

def search(request):
    return HttpResponse("We are at Search page")


def productView(request):
    return HttpResponse("We are at productView page")


def checkout(request):
    return HttpResponse("We are at checkout page")
