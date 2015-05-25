from maps.models import Marker
from rest_framework import serializers

# from closet.serializers import SubcategorySerializer


class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    subcategories = serializers.SerializerMethodField()

    def get_subcategories(self, obj):
        if obj:
            return [x.name for x in obj.subcategories.all()]

    class Meta:
        model = Marker
        fields = ('name', 'lat', 'lon', 'comment', 'subcategories', 'popup')
