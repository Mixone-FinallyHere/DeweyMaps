from maps.models import Map, Marker
from rest_framework import serializers


class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ('name', 'lat', 'lon', 'comment', 'tags_tuple')


class MapSerializer(serializers.HyperlinkedModelSerializer):
    markers = MarkerSerializer(many=True, read_only=True)

    class Meta:
        model = Map
        fields = ('name', 'markers')
