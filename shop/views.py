from django.shortcuts import redirect, render
from django.http import HttpResponse
from sympy import product
from .models import Product, Contact, Order
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
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        contact = Contact(name= name, email = email, subject = subject, message = message)
        contact.save()

    return render(request, 'shop/contact.html')

def checkout(request):
    if request.method == 'post':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '') 
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        
        order = Order(name=name, email=email, phone=phone, address=address, city=city, state=state,zip_code=zip_code)
        order.save()
        print("Order = ",order)

    return render(request, 'shop/checkout.html')

def tracker(request):
        return render(request, 'shop/tracker.html')


def search(request):
        return render(request, 'shop/search.html')


def productView(request, myid):
    # Fetch the product using id
    product = Product.objects.filter(id = myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})


# Excercise - 3. get product data and display it into index.html page.
# def get_data(request):
#     prod_data = Product.objects.all()
#     context = {'Product_data': prod_data}
#     return render(request, 'shop/get_data.html', context)
#***********************************************************************

