from django.contrib.gis.db import models

from closet.models import Subcategory


class Marker(models.Model):
    name = models.CharField(blank=False, max_length=255)
    position = models.PointField(geography=True, blank=False)
    comment = models.TextField(blank=True, null=False, default="")
    subcategories = models.ManyToManyField(Subcategory)
    web = models.URLField(default="")
    phone = models.CharField(max_length=15, default="")
    adress = models.CharField(max_length=1000, default="")
    public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

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

    @property
    def popup(self):
        tpl = """<h5>{0.name}</h5>"""
        if self.adress != "":
            tpl += "<em>Adresse</em> : {0.adress}<br><br>"
        if self.phone != "":
            tpl += "<em>Téléphone</em> : {0.phone}<br><br>"
        if self.web != "":
            tpl += '<b><a target="_blank" href="{0.web}">Site web</a></b><br><br>'

        tpl += "{0.comment}<br><br>"

        tpl += '<a href="http://dewey.be/contact.html" target="_blank">Signaler un problème</a>'

        return tpl.format(self)
