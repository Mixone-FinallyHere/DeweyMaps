from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator


class Map(models.Model):
    name = models.CharField(max_length=255)
    center = models.PointField(geography=True, blank=False)
    zoom = models.PositiveIntegerField(validators=[MaxValueValidator(18)])
    points = models.ManyToManyField('maps.Marker')
