from django import forms
from . import models


class StreetAddressForm(forms.ModelForm):
    class Meta:
        model = models.StreetAddress
        fields = [
            "street_address",
            "state",
            "country",
            "area",
            "object_id",
            "content_type",
        ]
