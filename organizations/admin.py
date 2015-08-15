from django.contrib import admin
from organizations.models import (
    Organization,
    OrganizationAdmin,
    OrganizationMember,
    OrganizationLink,
    OrganizationCategory,
    Category
)

admin.site.register(Organization)
admin.site.register(OrganizationAdmin)
admin.site.register(OrganizationMember)
admin.site.register(OrganizationLink)
admin.site.register(OrganizationCategory)
admin.site.register(Category)