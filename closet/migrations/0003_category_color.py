# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('closet', '0002_auto_20150525_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(default=333333, max_length=6),
            preserve_default=False,
        ),
    ]
