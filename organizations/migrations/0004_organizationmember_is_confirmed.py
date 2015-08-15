# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20150815_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationmember',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
