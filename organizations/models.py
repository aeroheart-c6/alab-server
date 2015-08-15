from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.db import models


optional = {'null': True, 'blank': True}

class Organization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
    administrators = models.ManyToManyField('users.User', **{
                         'related_name': 'organizations_managed',
                         'through': 'organizations.OrganizationAdmin',
                     })
    members = models.ManyToManyField('users.User', **{
                  'related_name': 'organizations',
                  'through': 'organizations.OrganizationMember',
              })
    children = models.ManyToManyField('self', **{
                   'related_name': 'parents',
                   'symmetrical': False,
                   'through': 'organizations.OrganizationLink',
                   'through_fields': ('parent', 'child'),
               })
    categories = models.ManyToManyField('organizations.Category', **{
                     'related_name': 'organizations',
                     'through': 'organizations.OrganizationCategory',
                 })


class OrganizationAdmin(models.Model):
    organization = models.ForeignKey('organizations.Organization')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime_added = models.DateTimeField(auto_now_add=True)


class OrganizationMember(models.Model):
    organization = models.ForeignKey('organizations.Organization')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime_joined = models.DateTimeField(auto_now_add=True)


class OrganizationLink(models.Model):
    parent = models.ForeignKey('organizations.Organization', related_name='+')
    child = models.ForeignKey('organizations.Organization', related_name='+')


class OrganizationCategory(models.Model):
    organization = models.ForeignKey('organizations.Organization')
    category = models.ForeignKey('organizations.Category')


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
