from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    pizzas = Product.objects.all()
    return render(request, "pizza/home.html",{"products":pizzas})