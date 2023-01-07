from rest_framework.viewsets import ModelViewSet

from orders.models import Shop, Product
from orders.serializers import ShopModelSerializer, ProductModelSerializer, CategoryModelSerializer


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategoryModelSerializer
