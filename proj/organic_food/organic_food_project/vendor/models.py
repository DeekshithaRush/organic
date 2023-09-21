# vendor/models.py
from django.db import models

class Vendor(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
class Product(models.Model):
    VEG = 'Vegetables'
    FRUIT = 'Fruits'
    CATEGORY_CHOICES = [
        (VEG, 'Vegetables'),
        (FRUIT, 'Fruits'),
    ]
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    quantity = models.PositiveIntegerField()
