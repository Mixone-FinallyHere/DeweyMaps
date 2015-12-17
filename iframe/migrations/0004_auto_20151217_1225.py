# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iframe', '0003_auto_20151202_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='points',
        ),
        migrations.RemoveField(
            model_name='map',
            name='uuid',
        ),
    ]
