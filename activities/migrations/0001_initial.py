# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('longitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('latitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('duration', models.DurationField()),
                ('datetime_held', models.DateTimeField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.ForeignKey(to='activities.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityParticipant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_joined', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(to='activities.Activity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='category',
            field=models.ForeignKey(to='activities.Category'),
        ),
        migrations.AddField(
            model_name='activity',
            name='categories',
            field=models.ManyToManyField(related_name='activities', through='activities.ActivityCategory', to='activities.Category'),
        ),
        migrations.AddField(
            model_name='activity',
            name='owner',
            field=models.ForeignKey(related_name='activities', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='activity',
            name='participants',
            field=models.ManyToManyField(related_name='activities', through='activities.ActivityParticipant', to=settings.AUTH_USER_MODEL),
        ),
    ]
