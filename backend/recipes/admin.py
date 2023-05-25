from django.conf import settings
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (Favorite, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag)


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug',
    )
    search_fields = ('name',)
    ordering = ('color',)
    empty_value_display = settings.EMPTY_VALUE


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
        'get_recipes_count',
    )
    search_fields = ('name',)
    ordering = ('measurement_unit',)
    empty_value_display = settings.EMPTY_VALUE

    def get_recipes_count(self, obj):
        return IngredientAmount.objects.filter(ingredient=obj.id).count()

    get_recipes_count.short_description = _('Использований в рецептах')


class RecipeIngredientsInline(admin.TabularInline):
    model = IngredientAmount
    min_num = 1
    extra = 1


@admin.register(IngredientAmount)
class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'ingredient',
        'amount',
    )
    list_filter = ('id', 'recipe', 'ingredient')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
    )
    list_filter = ('name', 'author', 'tags',)
    readonly_fields = ('in_favorite',)
    inlines = (RecipeIngredientsInline,)
    empty_value_display = settings.EMPTY_VALUE

    def in_favorite(self, obj):
        return obj.in_favorite.all().count()

    in_favorite.short_description = _('Количество добавлений в избранное')


@admin.register(Favorite)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )


@admin.register(ShoppingCart)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )
