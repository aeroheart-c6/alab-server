from __future__ import (
        absolute_import,
)

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


optional = {'null': True, 'blank': True}

class Organization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(**optional)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_premium = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, **optional)
    photo = models.ImageField(upload_to="organization/", **optional)
    
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

    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['name']
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')        


class OrganizationAdmin(models.Model):
    organization = models.ForeignKey('organizations.Organization')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{} ({})".format(self.organization, self.user)

    class Meta(object):
        ordering  = ['organization']
        verbose_name = _('Organization Administrator')
        verbose_name_plural = _('Organization Administrators')


class OrganizationMember(models.Model):
    organization = models.ForeignKey('organizations.Organization')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime_joined = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}, member of {}".format(self.user, self.organization)

    class Meta(object):
        ordering = ['user']
        verbose_name = _('Organization Member')
        verbose_name_plural = _('Organization Members')


class OrganizationLink(models.Model):
    parent = models.ForeignKey('organizations.Organization', related_name='+')
    child = models.ForeignKey('organizations.Organization', related_name='+')

    def __unicode__(self):
        return "{} incorporated with {}".format(self.child, self.parent)

    class Meta(object):
        ordering = ['child']
        verbose_name = _('Organization Link')
        verbose_name_plural = _('Organization Links')


class OrganizationCategory(models.Model):
    organization = models.ForeignKey('organizations.Organization')
    category = models.ForeignKey('organizations.Category')

    def __unicode__(self):
        return "{} as {}".format(self.organization, self.category)

    class Meta(object):
        ordering = ['organization']
        verbose_name = _('Organization Category')
        verbose_name_plural = _('Organization Categories')


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = ('Categories')
