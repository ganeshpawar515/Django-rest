from django.urls import path
from . import views

urlpatterns=[
    path("", views.getData),
    path("add/", views.addData),
    path("getJoke/", views.getJoke),
    path("update/<int:pk>",views.updateData)
]