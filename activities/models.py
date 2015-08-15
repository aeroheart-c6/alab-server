from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.db import models


optional = {'null': True, 'blank': True}

class Activity(models.Model):
    owner = models.ForeignKey('organizations.Organization', related_name='activities')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    longitude = models.DecimalField(max_digits=13, decimal_places=10)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    duration = models.DurationField()
    datetime_held = models.DateTimeField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    
    categories = models.ManyToManyField('activities.Category', through='activities.ActivityCategory')
    participants = models.ManyToManyField('users.User', through='activities.Participant')


class ActivityCategory(models.Model):
    activity = models.ForeignKey('activities.Activity')
    category = models.ForeignKey('activities.Category')


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()


class Participant(models.Model):
    activity = models.ForeignKey('activities.Activity')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime_joined = models.DateTimeField(auto_now_add=True)
