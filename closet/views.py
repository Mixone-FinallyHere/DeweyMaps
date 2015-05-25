from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from closet.models import Category, Subcategory
from closet.serializers import SubcategorySerializer, CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('subcategory_set').all()
    serializer_class = CategorySerializer
