from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from . models import Product, Category, SubCategory
from .views import ElectroList, MicroList, SubList
urlpatterns = [
    url(r'^$', views.electronic_base),
    url(r'^categories/$', ElectroList.as_view(template_name = "electronic/electronic_menu.html" )),
    url(r'^categories/micro/$', MicroList.as_view(
    	template_name= "electronic/micro_all.html")),
    url(r'^categories/micro/sub/$', views.categories_table),
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

