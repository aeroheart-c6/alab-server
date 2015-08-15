# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['name'], 'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterModelOptions(
            name='organizationadmin',
            options={'ordering': ['organization'], 'verbose_name': 'Organization Administrator', 'verbose_name_plural': 'Organization Administrators'},
        ),
        migrations.AlterModelOptions(
            name='organizationcategory',
            options={'ordering': ['organization'], 'verbose_name': 'Organization Category', 'verbose_name_plural': 'Organization Categories'},
        ),
        migrations.AlterModelOptions(
            name='organizationlink',
            options={'ordering': ['child'], 'verbose_name': 'Organization Link', 'verbose_name_plural': 'Organization Links'},
        ),
        migrations.AlterModelOptions(
            name='organizationmember',
            options={'ordering': ['user'], 'verbose_name': 'Organization Member', 'verbose_name_plural': 'Organization Members'},
        ),
        migrations.AddField(
            model_name='organization',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
