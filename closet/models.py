from django.db import models


class Category(models.Model):
    name = models.CharField(blank=False, max_length=255)


class Subcategory(models.Model):
    name = models.CharField(blank=False, max_length=255)
    category = models.ForeignKey(Category)
