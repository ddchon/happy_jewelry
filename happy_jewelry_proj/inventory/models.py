from django.db import models

# Create your models here.

class Product(models.Model):
    product_img = models.ImageField(upload_to='media')
    description = models.CharField(max_length=100)
    item_type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.description





