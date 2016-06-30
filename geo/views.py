from django.shortcuts import render
from django.http import HttpResponse
from . models import Category_geo, Geology

def geo_base(request):
	return render(request, 'geo/geo_menu.html')



# Create your views here.
