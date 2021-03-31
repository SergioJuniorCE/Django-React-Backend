from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    class Tax(models.TextChoices):
        EST = 'EST', 'Estandar'
        NIP = 'NIP', 'No imponible'
        PDG = 'PDG', 'Producto digital'
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    our_price = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax_type = models.CharField(max_length=200, choices=Tax.choices, null=True, blank=True, default=Tax.choices[0])
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    numReviews = models.IntegerField(default=0, null=True, blank=True)
    countInStock = models.IntegerField(default=0, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID {self.id}: {self.name}"
    

class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
