from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from . models import Geology, Category_geo

urlpatterns = [
    url(r'^$', views.geo_base),
    url(r'^result$', views.search),
    url(r'^ground/$', ListView.as_view(queryset = Geology.objects.filter(category__title__icontains="Наземное оборудование").order_by("-date")[:5],
    template_name = "geo/ground.html" )),
    url(r'^ground/(?P<pk>\d+)$', DetailView.as_view(model = Geology,
    	template_name= "geo/ground_detail.html")),
    url(r'^well/$', ListView.as_view(queryset = Geology.objects.filter(category__title__icontains="Скважинные").order_by("-title")[:5],
    template_name = "geo/well.html" )),
    url(r'^well/(?P<pk>\d+)$', DetailView.as_view(model = Geology,
    	template_name= "geo/well_detail.html")),
    url(r'^winch/$', ListView.as_view(queryset = Geology.objects.filter(category__title__icontains="Лебедки").order_by("-date")[:5],
    template_name = "geo/winch.html" )),
    url(r'^winch/(?P<pk>\d+)$', DetailView.as_view(model = Geology,
    	template_name= "geo/winch_detail.html")),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

