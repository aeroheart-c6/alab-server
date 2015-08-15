# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_organization_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationcategory',
            name='category',
            field=models.ForeignKey(related_name='+', to='organizations.Category'),
        ),
        migrations.AlterField(
            model_name='organizationcategory',
            name='organization',
            field=models.ForeignKey(related_name='+', to='organizations.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationmember',
            name='organization',
            field=models.ForeignKey(related_name='+', to='organizations.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationmember',
            name='user',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='organizationadmin',
            unique_together=set([('organization', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='organizationcategory',
            unique_together=set([('organization', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='organizationlink',
            unique_together=set([('parent', 'child')]),
        ),
        migrations.AlterUniqueTogether(
            name='organizationmember',
            unique_together=set([('organization', 'user')]),
        ),
    ]
