from django.contrib import admin
from .models import Product,Cart,CartItem, Order, OrderItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
