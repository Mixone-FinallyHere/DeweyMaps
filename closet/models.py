from django.db import models
from django.core.validators import RegexValidator


ColorValidator = RegexValidator(
    regex=r'^[A-Fa-f0-9]{6}$',
    message="Entrez une couleur valide (pas de '#' et 6 caractères)",
)


class Category(models.Model):
    name = models.CharField(blank=False, max_length=255)
    color = models.CharField(blank=False, max_length=6, validators=[ColorValidator])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    name = models.CharField(blank=False, max_length=255)
    category = models.ForeignKey(Category, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Sub-category"
        verbose_name_plural = "Sub-categories"
