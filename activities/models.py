from __future__ import (
    absolute_import,
)


from django.utils.translation import ugettext as _

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
    photo = models.ImageField(upload_to="event/", **optional)
    duration = models.DurationField()
    datetime_held = models.DateTimeField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField('activities.Category', **{
                  'related_name': 'activities',
                  'through': 'activities.ActivityCategory',
                 })
    participants = models.ManyToManyField('users.User', **{
                       'related_name': 'activities',
                       'through': 'activities.ActivityParticipant'
                   })

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __unicode__(self):
        return '{}'.format(self.title)


class ActivityCategory(models.Model):
    activity = models.ForeignKey('activities.Activity')
    category = models.ForeignKey('activities.Category')


class ActivityParticipant(models.Model):
    activity = models.ForeignKey('activities.Activity')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime_joined = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} - {}'.format(self.activity, self.user)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
