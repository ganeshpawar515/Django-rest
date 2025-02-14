from django.db import models

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