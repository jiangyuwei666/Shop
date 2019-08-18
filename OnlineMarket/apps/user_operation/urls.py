from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.user_operation.views import UserFavViewSet,UserCommentViewSet,UserAddressViewSet

router = DefaultRouter()
router.register('fav', UserFavViewSet)
router.register('comment', UserCommentViewSet)
router.register('addr', UserAddressViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
