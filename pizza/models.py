from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Size(models.Choices):
    SMALL = "s"
    MEDIUM = "m"
    LARGE = "l"

class Product(models.Model):
    PRODUCT_CHOICES=[
        ("pizza","Pizza"),
        ("cold drink","Cold Drink")
        ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=PRODUCT_CHOICES,default=PRODUCT_CHOICES[0][0])
    description = models.TextField(blank=True, null=True)
    
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="product_images/")
    
    size = models.CharField(
        max_length=2,
        choices=Size.choices,
        default=Size.SMALL
    )

    def __str__(self) -> str:
        return f"{self.name} {self.price}"
    def is_availaible(self):
        return True
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="orders")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"

    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.items.all())

class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="items")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def get_total_price(self):
        return self.product.price * self.quantity





