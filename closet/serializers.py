from closet.models import Category, Subcategory
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategories = serializers.SerializerMethodField()

    def get_subcategories(self, obj):
        if obj:
            return [{'id': x.id, 'name': x.name} for x in obj.subcategory_set.all().order_by('name')]

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')


class SubcategorySerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
