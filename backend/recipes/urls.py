from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientsViewSet, RecipeViewSet, TagsViewSet

app_name = 'recipes'

api_recipes_router_v1 = DefaultRouter()
api_recipes_router_v1.register(r'tags', TagsViewSet, basename='tags')
api_recipes_router_v1.register(r'ingredients', IngredientsViewSet,
                               basename='ingredients')
api_recipes_router_v1.register(r'recipes', RecipeViewSet,
                               basename='recipes')

urlpatterns = [
    path(r'', include(api_recipes_router_v1.urls)),
]
