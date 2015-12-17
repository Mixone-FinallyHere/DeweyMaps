from django import forms
from closet.models import Subcategory


class MapForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    zoom = forms.IntegerField()
    subcategories = forms.ModelMultipleChoiceField(
        queryset=Subcategory.objects.all(),
        required=False,
    )
