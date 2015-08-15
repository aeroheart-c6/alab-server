# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150815_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='instagram_token',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
