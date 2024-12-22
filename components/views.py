from django.shortcuts import render


def homepage(request):
    return render(request, 'components/index.html')


def contactus(request):
    return render(request, 'components/contactus.html')


def aboutus(request):
    return render(request, 'components/about.html')
