from django.db import models
from django.db.models import Model, CASCADE


class Category(Model):
    name = models.CharField(max_length=255)


class Product(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='')
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', CASCADE)
