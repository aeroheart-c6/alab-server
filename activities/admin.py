from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.contrib import admin

from activities.models import (
    Activity,
    ActivityParticipant
)

admin.site.register(Activity)
admin.site.register(ActivityParticipant)
