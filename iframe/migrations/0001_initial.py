# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import uuidfield.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_marker_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('center', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('zoom', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(18)])),
                ('uuid', uuidfield.fields.UUIDField(max_length=32, editable=False, blank=True, unique=True)),
                ('points', models.ManyToManyField(to='maps.Marker')),
            ],
        ),
    ]
