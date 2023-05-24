from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientsViewSet, RecipeViewSet, TagsViewSet

app_name = 'recipes'

recipes_router_v1 = DefaultRouter()
recipes_router_v1.register('tags', TagsViewSet)
recipes_router_v1 .register('ingredients', IngredientsViewSet),
recipes_router_v1 .register('recipes', RecipeViewSet),

urlpatterns = [
    path('', include(recipes_router_v1.urls)),
]
