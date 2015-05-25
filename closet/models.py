from django.db import models


class Category(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    name = models.CharField(blank=False, max_length=255)
    category = models.ForeignKey(Category)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Sub-category"
        verbose_name_plural = "Sub-categories"
