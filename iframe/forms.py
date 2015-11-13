from django.forms import ModelForm
from iframe.models import Map


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'center', 'zoom']
