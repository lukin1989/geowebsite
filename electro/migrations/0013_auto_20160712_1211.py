# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 06:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electro', '0012_auto_20160712_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='values',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=set(["'values' : []"])),
        ),
    ]
