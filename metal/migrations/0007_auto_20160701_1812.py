# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0006_category_metal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_metal',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category_metal',
            name='image',
        ),
        migrations.AddField(
            model_name='metal',
            name='title',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]
