from django.shortcuts import render
from django.http import HttpResponse
from .models import Category_metal, Metal
#from . models import 
def metal_base(request):
	metal_all = Metal.objects.filter(category__title__icontains="Металлообработка")
	return render(request,'metal/metal_main.html', {'metal_all': metal_all})


