from __future__ import (
    absolute_import,
)

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Transaction(models.Model):
    ITEM_DUMMY = 0 # DO NOT USE THIS IN PRODUCTION
    ITEM_DONATION = 1
    ITEM_VERIFY_ORG = 2
    ITEM_PREMIUM_ORG = 3
    ITEM_CHOICES = (
        (ITEM_DUMMY, 'Dummy Purchase'),
        (ITEM_VERIFY_ORG, 'Verified Organization'),
        (ITEM_PREMIUM_ORG, 'Premium Organization'),
    )
    
    creator_type = models.ForeignKey(ContentType)
    creator_id = models.PositiveIntegerField()
    creator = GenericForeignKey('creator_type', 'creator_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.PositiveSmallIntegerField(default=ITEM_DUMMY, choices=ITEM_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
