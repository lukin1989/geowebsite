from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from . models import Category_metal, Metal

urlpatterns = [
    url(r'^$', views.metal_base, name = "metal"), 
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Metal,
        template_name= "metal/metal_detail.html")),


] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

