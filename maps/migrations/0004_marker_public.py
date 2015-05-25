# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20150525_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
