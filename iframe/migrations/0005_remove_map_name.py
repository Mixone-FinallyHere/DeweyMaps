# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iframe', '0004_auto_20151217_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='name',
        ),
    ]
