from django.contrib import admin
from . models import Geology, Category_geo, Category_new


admin.site.register(Category_geo)
admin.site.register(Category_new)
admin.site.register(Geology)

# Register your models here.
