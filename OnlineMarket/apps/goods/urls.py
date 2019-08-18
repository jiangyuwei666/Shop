from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.goods.views import GoodsViewSet, GoodsCategoryViewSet, BannerViewSet

router = DefaultRouter()
router.register(r'goods', GoodsViewSet)
router.register(r'categories', GoodsCategoryViewSet)
router.register(r'banners', BannerViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
