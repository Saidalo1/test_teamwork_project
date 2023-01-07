from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from orders.models import Shop, Product
from orders.serializers import ShopModelSerializer, ProductModelSerializer, CategoryModelSerializer
from shared.django import delete_main_photo


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    parser_classes = (MultiPartParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = {'price': ['gte', 'lte'], 'category': ['exact'], 'shop': ['exact']}
    search_fields = ('name',)

    def destroy(self, request, *args, **kwargs):
        delete_main_photo(Product, kwargs['pk'])
        return super().destroy(request, *args, **kwargs)


class CategoryModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategoryModelSerializer
