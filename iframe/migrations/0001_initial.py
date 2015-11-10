# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_marker_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('center', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('zoom', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(18)])),
                ('points', models.ManyToManyField(to='maps.Marker')),
            ],
        ),
    ]
