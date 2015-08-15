from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _


optional = {'null': True, 'blank': True}

class User(AbstractUser):
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class UserProfile(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, **optional)
    age = models.PositiveSmallIntegerField(**optional)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, **optional)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, **optional)
    address = models.CharField(max_length=500, **optional)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100, **optional)
    photo = models.ImageField(upload_to="user/", **optional)
    
    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __unicode__(self):
        return self.user.full_name
