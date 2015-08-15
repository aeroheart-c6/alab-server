# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20150815_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='longitude',
        ),
    ]
