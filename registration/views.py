from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, AccountChangeForm
from django.contrib.auth import authenticate, login, logout
from .models import Account, AddToCart
from products.models import Product


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'], )
            login(request, new_user)

            return redirect("components:homePage")

    context = {
        'form': form,
    }
    return render(request, "registration/registration.html", context)


def login_page(request):
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request.POST or None)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(email=str(data['email']), password=str(data['password']))

            if user is not None:
                login(request, user)
                print(request.POST.get('next'))
                if request.POST.get('next'):
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('components:homePage')

    context = {
        'login_form': login_form,
    }

    return render(request, 'registration/login.html', context)


def account_edit(request):
    form = AccountChangeForm(instance=Account.objects.get(id=request.user.id))

    if request.method == 'POST':
        form = AccountChangeForm(request.POST, instance=Account.objects.get(id=request.user.id))
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }

    return render(request, 'registration/accountpage.html', context)


def logout_page(request):
    logout(request)
    return redirect('components:homePage')


def cart(request):
    carts = AddToCart.objects.filter(user=request.user)
    sum_price = 0
    for i in carts:
        sum_price += int(i.product.price)

    context = {
        'carts': carts,
        'sum_price': sum_price,
    }

    return render(request, 'registration/checkout.html', context)


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    user = request.user

    cart = AddToCart.objects.create(user=user, product=product)
    cart.save()

    return redirect("products:products")


def delete_cart(request, id):
    AddToCart.objects.get(id=id).delete()

    return redirect("registration:cart")
