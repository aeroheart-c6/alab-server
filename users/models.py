from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


optional = {'null': True, 'blank': True}

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    gender = models.CharField(max_length=1, default=GENDER_MALE, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField(default=16)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)
