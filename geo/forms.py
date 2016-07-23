
from django import forms

class GeoSearch(forms.Form):
    search_geo = forms.CharField(label='Search', max_length=200)
