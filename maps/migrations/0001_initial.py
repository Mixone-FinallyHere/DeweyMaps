# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('closet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True)),
                ('comment', models.TextField(blank=True, default='')),
                ('json_data', models.TextField(blank=True, default='{}')),
                ('subcategories', models.ManyToManyField(to='closet.Subcategory')),
            ],
        ),
    ]
