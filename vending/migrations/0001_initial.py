# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator_id', models.PositiveIntegerField()),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('item', models.PositiveSmallIntegerField(default=0, choices=[(0, b'Dummy Purchase'), (2, b'Verified Organization'), (3, b'Premium Organization')])),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('creator_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
    ]
