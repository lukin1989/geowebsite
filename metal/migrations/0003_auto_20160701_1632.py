# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0002_auto_20160701_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='')),
                ('image2', models.FileField(blank=True, upload_to='')),
                ('image3', models.FileField(blank=True, upload_to='')),
                ('image4', models.FileField(blank=True, upload_to='')),
                ('image5', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='category_metal',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category_metal',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category_metal',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='category_metal',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='category_metal',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='category_metal',
            name='image5',
        ),
        migrations.AddField(
            model_name='metal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metal.Category_metal'),
        ),
    ]
