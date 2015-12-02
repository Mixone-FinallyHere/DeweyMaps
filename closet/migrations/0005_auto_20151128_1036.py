# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import closet.models


class Migration(migrations.Migration):

    dependencies = [
        ('closet', '0004_auto_20150528_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(validators=[closet.models.ColorValidator], max_length=6),
        ),
    ]
