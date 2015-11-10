from iframe.models import Map
from rest_framework import serializers
from maps.serializers import MarkerSerializer


class MapSerializer(serializers.HyperlinkedModelSerializer):
    points = MarkerSerializer(many=True, read_only=True)

    class Meta:
        model = Map
        fields = ('name', 'points', 'center_lat', 'center_lon', 'zoom')
