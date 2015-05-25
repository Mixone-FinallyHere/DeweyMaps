# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_remove_marker_json_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='adress',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='marker',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='marker',
            name='web',
            field=models.URLField(default=''),
        ),
    ]
