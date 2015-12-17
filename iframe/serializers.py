from iframe.models import Map
from rest_framework import serializers
from maps.serializers import MarkerSerializer
from closet.models import Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    marker_set = MarkerSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ('name', 'marker_set',)


class MapSerializer(serializers.ModelSerializer):
    points = MarkerSerializer(many=True, read_only=True)
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Map
        fields = ('points', 'center_lat', 'center_lon', 'zoom', 'subcategories')
