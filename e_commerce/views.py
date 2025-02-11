from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "e_commerce/indes.html")

def cart(request):
    return render(request, "e_commerce/cart.html")