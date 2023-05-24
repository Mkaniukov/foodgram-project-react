from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

app_name = 'users'

api_router_v1 = DefaultRouter()
api_router_v1.register('users', CustomUserViewSet)
urlpatterns = [
    path(r'', include(api_router_v1.urls)),
    path(r'', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
