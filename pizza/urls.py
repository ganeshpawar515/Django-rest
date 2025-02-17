from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path("getcart/",views.cart, name="get_cart"),
    path("add_to_cart/<int:product_id>/",views.cart, name="add_to_cart"),
    path("cart_remove_all/",views.cart_remove_all,name="cart_remove_all"),
    path("order/",views.order,name="orders")
]