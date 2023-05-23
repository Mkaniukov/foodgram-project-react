from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientsViewSet, RecipeViewSet, TagsViewSet

app_name = 'recipes'

router_v1 = DefaultRouter()
router_v1.register('tags', TagsViewSet)
router_v1.register('ingredients', IngredientsViewSet),
router_v1.register('recipes', RecipeViewSet),

urlpatterns = [
    path('', include(router_v1.urls)),
]
