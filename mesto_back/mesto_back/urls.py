"""mesto_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

from django.conf.urls import url
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cards.views import CardViewSet, UserViewSet

from rest_framework.authtoken import views
from cards.views import user_patch, like_card


router = DefaultRouter()
# router.register(r'cards/likes/(?P<card_id>\d+)', LikeViewSet)
router.register(r'cards', CardViewSet)
router.register(r'users', UserViewSet)
# router.register(r'cards/likes/(?P<card_id>\d+)/', LikeViewSet,
#                 basename='likes')
# router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/users/me/', user_patch),
    path('v1/users/me/avatar/', user_patch),
    url(r'^v1/cards/likes/(?P<card_id>\d+)/$', like_card),
    path('v1/', include(router.urls)),

    # url(r'^swagger(?P<format>\.json|\.yaml)$',
    #     schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
    #     name='schema-swagger-ui'),
    # если аутентификация по Token
    # path('api-token-auth/', views.obtain_auth_token),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('v1/auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/auth/', include('djoser.urls.jwt')),

]

# if settings.DEBUG:
#
# urlpatterns += static(settings.MEDIA_URL)