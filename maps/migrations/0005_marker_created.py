# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_marker_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 25, 11, 22, 29, 549955, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
