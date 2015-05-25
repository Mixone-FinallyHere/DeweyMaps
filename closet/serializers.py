from closet.models import Category, Subcategory
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategories = serializers.SerializerMethodField()

    def get_subcategories(self, obj):
        if obj:
            return [x.id for x in obj.subcategory_set.all()]

    class Meta:
        model = Category
        fields = ('name', 'subcategories')


class SubcategorySerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
