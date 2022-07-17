from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


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

# Excercise - 3. get product data and display it into index.html page.
def get_data(request):
    prod_data = Product.objects.all()
    # one_data = 
    context = {'Product_data' : prod_data}
    return render(request, 'shop/get_data.html', context)