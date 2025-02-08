from django.urls import path
from . import views

urlpatterns=[
    path("",views.home),
    path("farm/",views.farmProduct),
    path("farm/<int:id>/",views.farmProduct),
    path('order/',views.manageOrder),
    path('order/<int:id>',views.manageOrder),
]