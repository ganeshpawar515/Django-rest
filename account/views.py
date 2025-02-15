from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import *
# Create your views here.

def createUser(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form=SignUpForm()
    form = SignUpForm()
    return render(request,"account/create_user.html",{"form":form})