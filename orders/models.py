from django.db.models import Model, CASCADE, CharField, IntegerField, ImageField, ForeignKey


class Shop(Model):
    name = CharField(max_length=255)


class Category(Model):
    name = CharField(max_length=255)


class SubCategory(Model):
    name = CharField(max_length=50)
    category = ForeignKey(Category, CASCADE)

    def __str__(self):
        return f'{self.category.name} --> {self.name}'

    class Meta:
        db_table = 'sub_category'


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField(default=0)
    img = ImageField(upload_to='products/')
    description = CharField(max_length=500)
    category = ForeignKey('Category', CASCADE)
    shop = ForeignKey('Shop', CASCADE)
