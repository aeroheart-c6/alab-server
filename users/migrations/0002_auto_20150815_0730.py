# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveSmallIntegerField(default=16, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, null=True, blank=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=13, decimal_places=10, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=13, decimal_places=10, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='timezone',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
