from django.shortcuts import render
from django.http import HttpResponse
#from . models import 

def metal_base(request):
	return render(request, 'metal/metal_main.html')
