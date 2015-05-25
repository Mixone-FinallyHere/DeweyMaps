from django.shortcuts import render
from closet.models import Category, Subcategory


def index(request):
    context = {
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
    }
    return render(request, 'www/index.html', context)
