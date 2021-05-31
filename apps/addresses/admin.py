from django.contrib import admin
from django import forms

from . import models


class StreetAddressAdminForm(forms.ModelForm):

    class Meta:
        model = models.StreetAddress
        fields = "__all__"


class StreetAddressAdmin(admin.ModelAdmin):
    form = StreetAddressAdminForm
    list_display = [
        "street_address",
        "area",
        "state",
        "country",
        "address_owner",
        # "object_id",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "street_address",
        # "area",
        # "state",
        # "country",
        # "object_id",
        # "address_owner",
        "created",
        "last_updated",
    ]


admin.site.register(models.StreetAddress, StreetAddressAdmin)
