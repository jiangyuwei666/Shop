from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.trade.views import ShoppingCartViewSet, OrderInfoViewSet, OrderGoodsViewSet

router = DefaultRouter()

router.register('shopping_cart', ShoppingCartViewSet)
router.register('order_info', OrderInfoViewSet)
router.register('order_goods', OrderGoodsViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
