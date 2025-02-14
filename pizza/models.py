from django.db import models

# Create your models here.
class Size(models.Choices):
    Small = "s"
    Medium = "m"
    Large = "l"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField()
    
    size = models.CharField(
        max_length=1,
        choices=Size.choices,
        default=Size.Small
    )

    def __str__(self) -> str:
        return f"{self.name} {self.price}"
    def is_availaible(self):
        return True