from rest_framework.serializers import ModelSerializer

from orders.models import Shop, Product, Category, SubCategory


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        exclude = ()


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class SubCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        exclude = ()
