# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('longitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('latitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_added', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(to='organizations.Organization')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='organizations.Category')),
                ('organization', models.ForeignKey(to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('child', models.ForeignKey(related_name='+', to='organizations.Organization')),
                ('parent', models.ForeignKey(related_name='+', to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_joined', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(to='organizations.Organization')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='administrators',
            field=models.ManyToManyField(related_name='organizations_managed', through='organizations.OrganizationAdmin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='categories',
            field=models.ManyToManyField(related_name='organizations', through='organizations.OrganizationCategory', to='organizations.Category'),
        ),
        migrations.AddField(
            model_name='organization',
            name='children',
            field=models.ManyToManyField(related_name='parents', through='organizations.OrganizationLink', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(related_name='organizations', through='organizations.OrganizationMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
