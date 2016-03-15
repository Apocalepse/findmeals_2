# -*- coding: utf-8 -*-
from django.contrib import admin
from recipe_search.models import *


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Variation)
admin.site.register(RecipeIngredient)
