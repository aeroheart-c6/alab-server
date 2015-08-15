from __future__ import (
    absolute_import,
)


from django import forms
from django.template.defaultfilters import slugify

from activities.models import Activity


class ActivityForm(forms.ModelForm):

    datetime_end = forms.DateTimeField()

    class Meta:
        model = Activity
        exclude = (
            'categories',
            'duration',
            'slug',
        )

    def save(self, commit=True):
        activity = super(ActivityForm, self).save(commit=False)

        if commit:
            activity.slug = slugify(self.cleaned_data['title'])
            activity.duration = self.cleaned_data['datetime_end'] - self.cleaned_data['datetime_held']
            activity.save()

        return activity
