from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')