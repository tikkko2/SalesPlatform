from unicodedata import category
from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/allproduct.html', context)


def filtered_products(request):
    if request.GET.get('sort-item') == "ascending":
        products = Product.objects.all().order_by('price')
    elif request.GET.get('sort-item') == "descending":
        products = Product.objects.all().order_by('-price')
    elif request.GET.get('sort-item') == "normal":
        products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/allproduct.html', context)


def single_product(request, id):
    product = Product.objects.get(id=id)

    context = {

        'product': product,

    }

    return render(request, 'products/oneproduct.html', context)


def women(request):
    women = Product.objects.filter(category='2')

    context = {
        'women': women
    }

    return render(request, 'products/women.html', context)


def men(request):
    men = Product.objects.filter(category='1')

    context = {
        'men': men
    }

    return render(request, 'products/men.html', context)


def kids(request):
    kids = Product.objects.filter(category='5')

    context = {
        'kids': kids
    }

    return render(request, 'products/kids.html', context)
