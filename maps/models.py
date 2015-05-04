from django.contrib.gis.db import models
from taggit.managers import TaggableManager


class Map(models.Model):
    name = models.CharField(blank=False, max_length=255)
    template = models.TextField(blank=False, default="{{ obj.comment }}")

    def __str__(self):
        return self.name


class Marker(models.Model):
    name = models.CharField(blank=False, max_length=255)
    position = models.PointField(geography=True, blank=False)
    comment = models.TextField(blank=True, null=False, default="")
    mp = models.ForeignKey(Map, name="map", related_name="markers")

    objects = models.GeoManager()
    tags = TaggableManager()

    def __str__(self):
        return self.name

    @property
    def content(self):
        return self.comment

    @property
    def tags_tuple(self):
        return [(tag.slug, tag.name) for tag in self.tags.all()]

    @property
    def lat(self):
        return self.position.y

    @property
    def lon(self):
        return self.position.x
