import json

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
    mp = models.ForeignKey(Map, name="map")

    objects = models.GeoManager()
    tags = TaggableManager()

    def __str__(self):
        return self.name

    @property
    def content(self):
        return self.comment

    def jsonable(self):
        return {
            'name': self.name,
            'position': json.loads(self.position.json),
            'comment': self.comment,
            'tags': list(map(lambda x: {'name': x.name, 'slug': x.slug}, self.tags.all()))
        }
