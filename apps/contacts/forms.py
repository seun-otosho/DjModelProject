from django import forms
from . import models


class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = models.ContactDetail
        fields = [
            "object_id",
            "contact_info",
            "type",
            "content_type",
        ]


class ContactCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ContactCategory
        fields = [
            "contact_type",
        ]
