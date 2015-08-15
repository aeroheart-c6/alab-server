# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_activity_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitycategory',
            options={'verbose_name': 'Activity Category', 'verbose_name_plural': 'Activity Categories'},
        ),
        migrations.AlterModelOptions(
            name='activityparticipant',
            options={'verbose_name': 'Activity Participant', 'verbose_name_plural': 'Activity Participants'},
        ),
        migrations.AlterField(
            model_name='activitycategory',
            name='activity',
            field=models.ForeignKey(related_name='+', to='activities.Activity'),
        ),
        migrations.AlterField(
            model_name='activitycategory',
            name='category',
            field=models.ForeignKey(related_name='+', to='activities.Category'),
        ),
        migrations.AlterField(
            model_name='activityparticipant',
            name='activity',
            field=models.ForeignKey(related_name='+', to='activities.Activity'),
        ),
        migrations.AlterField(
            model_name='activityparticipant',
            name='user',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='activitycategory',
            unique_together=set([('activity', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='activityparticipant',
            unique_together=set([('activity', 'user')]),
        ),
    ]
