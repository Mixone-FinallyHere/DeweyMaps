# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('maps', '0002_auto_20150502_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.'),
        ),
    ]
