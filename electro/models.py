from django.db import models
from django.contrib.postgres.fields import JSONField

class Category(models.Model):
	title = models.CharField(max_length = 200, verbose_name = "Название")
	def __str__(self):
		return self.title

class SubCategory(models.Model):
	title = models.CharField(max_length = 200 , verbose_name = "Название")
	category = models.ForeignKey(Category, verbose_name = "Категория")
	name = models.CharField("Название для таблицы",max_length=80, blank=True)
	feature1 = models.CharField("Характеристика товара",max_length=80, blank=True)
	feature2 = models.CharField("Характеристика товара",max_length=80, blank=True)
	feature3 = models.CharField("Характеристика товара",max_length=80, blank=True)
	feature4 = models.CharField("Характеристика товара",max_length=80, blank=True)
	feature5 = models.CharField("Характеристика товара",max_length=80, blank=True)
	price = models.CharField(default = "Цена товара, Сом", max_length=80, blank=True)
	def __str__(self):
		return self.title

class Product(models.Model):
	title = models.CharField(max_length = 200, verbose_name = "Название")
	category = models.ForeignKey(Category, verbose_name = "Категория")
	subcategory = models.ForeignKey(SubCategory, verbose_name = "Подкатегория")
	values = JSONField(default = {"values":[]})
	description = models.TextField(blank = True, verbose_name = "Описание ")
	price = models.IntegerField(default = 0)
	date= models.DateTimeField('Дата добавления')
	def __str__(self):
	 	return self.title


# Create your models here.
