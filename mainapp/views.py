from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def products(request):
    return render(request, 'mainapp/products.html')


def product_1(request):
    return render(request, 'mainapp/products/product_1.html')
