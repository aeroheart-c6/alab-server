# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150815_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
