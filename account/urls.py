from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns=[
    path("signup/",views.createUser, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html",authentication_form=LoginForm),name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page="login"), name="logout")
]