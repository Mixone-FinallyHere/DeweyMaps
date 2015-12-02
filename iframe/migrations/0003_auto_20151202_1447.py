# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iframe', '0002_map_subcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='points',
            field=models.ManyToManyField(blank=True, to='maps.Marker'),
        ),
        migrations.AlterField(
            model_name='map',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='closet.Subcategory'),
        ),
    ]
