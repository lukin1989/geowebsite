# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro', '0003_auto_20160706_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='feature1',
            field=models.CharField(blank=True, max_length=80, verbose_name='Характеристика товара'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='feature2',
            field=models.CharField(blank=True, max_length=80, verbose_name='Характеристика товара'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='feature3',
            field=models.CharField(blank=True, max_length=80, verbose_name='Характеристика товара'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='feature4',
            field=models.CharField(blank=True, max_length=80, verbose_name='Характеристика товара'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='feature5',
            field=models.CharField(blank=True, max_length=80, verbose_name='Характеристика товара'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
