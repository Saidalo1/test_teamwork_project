from rest_framework.routers import DefaultRouter

from orders.views import ShopModelViewSet, CategoryModelViewSet, ProductModelViewSet, SubCategoryModelViewSet

router = DefaultRouter()

router.register('shop', ShopModelViewSet)
router.register('category', CategoryModelViewSet)
router.register('subcategory', SubCategoryModelViewSet)
router.register('product', ProductModelViewSet)

urlpatterns = [

              ] + router.urls
