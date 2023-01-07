from django.db.models import Model, CASCADE, CharField, IntegerField, ImageField, ForeignKey


class Shop(Model):
    name = CharField(max_length=255)


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField(default=0)
    img = ImageField(upload_to='products/')
    description = CharField(max_length=500)
    category = ForeignKey('Category', CASCADE)
    shop = ForeignKey('Shop', CASCADE)
