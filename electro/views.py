from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, SubCategory
from django.views.generic import ListView, DetailView

def electronic_micro(request):
	micro_all = SubCategory.objects.filter(category__title__icontains="Микросхемы")
	return render(request,'electronic/micro_all.html', {'micro_all': micro_all})

def electronic_base(request):
	return render (request, "electronic/electronic_base.html")

class MicroList(ListView):
	model = SubCategory
	micro = SubCategory.objects.filter(category__title__icontains="Микросхемы")

class ElectroList(ListView):
	model = Category
	electro = Category.objects.all

class SubList(ListView):
	model = Product
	electro = Product.objects.filter(subcategory__title__icontains="Аналаговые")

def categories_table(request):
	subcategory_all = Product.objects.filter(subcategory__title__icontains="Аналаговые")
	subcategory_one = SubCategory.objects.get(title__icontains="Аналаговые")
	return render(request,'electronic/subcategory_table.html', {'subcategory_all': subcategory_all,
	 'subcategory_one': subcategory_one})

