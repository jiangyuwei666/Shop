from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
