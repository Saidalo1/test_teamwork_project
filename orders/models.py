from django.db.models import Model, CASCADE, CharField, IntegerField, ImageField, ForeignKey, DecimalField, PROTECT, \
    TextField, SET_NULL


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
    price = DecimalField(max_digits=9, decimal_places=2, default=0)
    img = ImageField(upload_to='products/')
    description = TextField()
    category = ForeignKey('orders.Category', CASCADE)
    shop = ForeignKey('orders.Shop', SET_NULL, null=True, blank=True)
