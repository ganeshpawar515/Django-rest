from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url="login")
def home(request):
    pizzas = Product.objects.all()
    return render(request, "pizza/home.html",{"products":pizzas})
@login_required(login_url="login")
def cart(request):
    return render(request, "pizza/getCart.html")