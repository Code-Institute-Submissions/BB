from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'base.html')

def Products(request):
    return render(request, 'products.html')
