from django.db import models

# Create your models here.

class Product(models.Model):
    PRODUCT_CHOICES=[
        ('electronic','Electronic'),
        ('clothing','Clothing'),
        ('food','Food')
        ]
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=PRODUCT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    