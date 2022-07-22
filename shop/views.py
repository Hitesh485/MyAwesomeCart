from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from math import ceil, prod


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = (n//4 + ceil((n/4) - (n//4)))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    print("cats = ", cats)

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = (n//4 + ceil((n/4) - (n//4)))
        allProds.append([prod, range(1,nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
        return render(request, 'shop/contact.html')


def tracker(request):
        return render(request, 'shop/tracker.html')


def search(request):
        return render(request, 'shop/search.html')


def productView(request):
        return render(request, 'shop/prodView.html')


def checkout(request):
    return HttpResponse("We are at checkout page")

# Excercise - 3. get product data and display it into index.html page.

def get_data(request):
    prod_data = Product.objects.all()
    context = {'Product_data': prod_data}
    return render(request, 'shop/get_data.html', context)
