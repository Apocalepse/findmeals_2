# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0418\u043d\u0433\u0440\u0438\u0434\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u0418\u043d\u0433\u0440\u0438\u0434\u0438\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0446\u0435\u043f\u0442',
                'verbose_name_plural': '\u0420\u0435\u0446\u0435\u043f\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_search.Recipe', verbose_name=b'\xd0\xa0\xd0\xb5\xd1\x86\xd0\xb5\xd0\xbf\xd1\x82')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_search.Ingredient', verbose_name='\u0418\u043d\u0433\u0440\u0438\u0434\u0438\u0435\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0446\u0435\u043f\u0442',
                'verbose_name_plural': '\u0420\u0435\u0446\u0435\u043f\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_search.Variation', verbose_name='\u0412\u0430\u0440\u0438\u0430\u0446\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='variations',
            field=models.ManyToManyField(through='recipe_search.RecipeIngredient', to='recipe_search.Variation', verbose_name='\u0412\u0430\u0440\u0438\u0430\u0446\u0438\u0438 \u0438\u0433\u043d\u0440\u0438\u0434\u0438\u0435\u043d\u0442\u043e\u0432'),
        ),
    ]
