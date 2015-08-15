# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20150815_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'event/', blank=True),
        ),
    ]
