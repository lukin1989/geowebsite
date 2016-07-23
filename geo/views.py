from django.shortcuts import render
from django.http import HttpResponse
from . models import Category_geo, Geology
from .forms import GeoSearch

def geo_base(request):
	return render(request, 'geo/geo_menu.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
	    q = request.GET['q']
	    result = Geology.objects.filter(title__icontains=q)
	    return render(request, 'geo/geo_results.html',{'result': result, 'query': q})
	else:
		return render(request, 'geo/geo_results.html', {'error': True})

