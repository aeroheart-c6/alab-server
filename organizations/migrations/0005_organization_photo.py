# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_organizationmember_is_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'organization/', blank=True),
        ),
    ]
