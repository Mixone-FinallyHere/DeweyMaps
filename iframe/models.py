from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator
from uuidfield import UUIDField


class Map(models.Model):
    name = models.CharField(max_length=255)
    center = models.PointField(geography=True, blank=False)
    zoom = models.PositiveIntegerField(validators=[MaxValueValidator(18)])
    points = models.ManyToManyField('maps.Marker', blank=True)
    subcategories = models.ManyToManyField('closet.Subcategory', blank=True)

    uuid = UUIDField(auto=True)

    @property
    def center_lat(self):
        return self.center.y

    @property
    def center_lon(self):
        return self.center.x
