from django import forms

from organizations.models import Organization
from slugify import slugify

class OrganizationApplicationForm(forms.Form):
    name = forms.CharField(max_length=200)
    address = forms.CharField(max_length=500)
    city = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    is_premium = forms.BooleanField(required=False)

    def save(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        slug = slugify(name)
        address = self.cleaned_data.get('address')
        city = self.cleaned_data.get('city')
        country = self.cleaned_data.get('country')
        is_premium = self.cleaned_data.get('is_premium')

        obj = Organization.objects.create(
            name=name,
            slug=slug,
            address=address,
            city=city,
            country=country,
            is_premium=is_premium,
        )
        # Please do not judge my code. I have purpose for this later. Lol.

        obj.save()
        return obj
