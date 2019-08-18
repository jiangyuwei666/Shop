"""OnlineMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve
from OnlineMarket.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework.authtoken import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title="XXX")),

    # url(r'login/', obtain_jwt_token),
    # url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'api/v1/goods/', include("apps.goods.urls")),
    url(r'api/v1/users/', include("apps.users.urls")),
    url(r'api/v1/user_operations/', include("apps.user_operation.urls")),
    url(r'api/v1/trades/', include("apps.trades.urls")),
]
