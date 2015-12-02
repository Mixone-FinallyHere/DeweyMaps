from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget
from iframe.models import Map


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'center', 'zoom']
        widgets = {'center': LeafletWidget()}
