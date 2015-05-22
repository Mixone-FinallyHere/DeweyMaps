from django.contrib.gis.db import models

from closet.models import Subcategory


class Marker(models.Model):
    name = models.CharField(blank=False, max_length=255)
    position = models.PointField(geography=True, blank=False)
    comment = models.TextField(blank=True, null=False, default="")
    json_data = models.TextField(blank=True, null=False, default="{}")
    subcategories = models.ManyToManyField(Subcategory)

    objects = models.GeoManager()

    def __str__(self):
        return self.name

    @property
    def content(self):
        return self.comment

    @property
    def lat(self):
        return self.position.y

    @property
    def lon(self):
        return self.position.x
