# -*- coding: utf-8 -*-
from django.db import models


class Recipe(models.Model):
    title = models.CharField(u'Название', max_length=255)
    variations = models.ManyToManyField('Variation', through='RecipeIngredient', verbose_name=u'Вариации игнридиентов')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Рецепт'
        verbose_name_plural = u'Рецепты'


class Ingredient(models.Model):
    title = models.CharField(u'Название', max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Ингридиент'
        verbose_name_plural = u'Ингридиенты'


class Variation(models.Model):
    ingredient = models.ForeignKey(Ingredient, verbose_name=u'Ингридиент')

    def __unicode__(self):
        return u'v%s, %s' % (self.pk, self.ingredient.title)

    class Meta:
        verbose_name = u'Вариация'
        verbose_name_plural = u'Вариации'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=u'Рецепт')
    variation = models.ForeignKey(Variation, verbose_name=u'Вариация')
