from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path("getcart/",views.cart, name="getcart"),
    path("add_to_cart/<int:product_id>/",views.cart, name="addtocart")
]