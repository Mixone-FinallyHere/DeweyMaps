# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closet', '0005_auto_20151128_1036'),
        ('iframe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='subcategories',
            field=models.ManyToManyField(to='closet.Subcategory'),
        ),
    ]
