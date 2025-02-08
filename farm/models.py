from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES=[
        ('vegetable','Vegetable'),
        ('fruit','Fruit'),
        ('grain','Grain'),
        ('dairy','Dairy'),
        ('other','Other')
    ]
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled')
    ]
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10,decimal_places=2,editable=False)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)

    def save(self,*args, **kwargs):
        if not self.pk:
            self.total_price = self.quantity * self.product.price
        super().save(*args,**kwargs)
    def __str__(self) -> str:
        return f"Order {self.id} - {self.product.name}"
