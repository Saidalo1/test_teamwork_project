from rest_framework.routers import DefaultRouter

from orders.views import ShopModelViewSet, CategoryModelViewSet, ProductModelViewSet

router = DefaultRouter()

router.register('shop', ShopModelViewSet)
router.register('category', CategoryModelViewSet)
router.register('product', ProductModelViewSet)

urlpatterns = [

              ] + router.urls