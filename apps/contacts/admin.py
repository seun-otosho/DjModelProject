from django.contrib import admin
from django import forms

from . import models


class ContactDetailAdminForm(forms.ModelForm):

    class Meta:
        model = models.ContactDetail
        fields = "__all__"


class ContactDetailAdmin(admin.ModelAdmin):
    form = ContactDetailAdminForm
    list_display = [
        "contact_info",
        "type",
        "contact_owner",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "object_id",
        # "contact_owner",
        # "contact_info",
        "last_updated",
        "created",
    ]


class ContactCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.ContactCategory
        fields = "__all__"


class ContactCategoryAdmin(admin.ModelAdmin):
    form = ContactCategoryAdminForm
    list_display = [
        "contact_type",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "contact_type",
        "created",
        "last_updated",
    ]


admin.site.register(models.ContactDetail, ContactDetailAdmin)
admin.site.register(models.ContactCategory, ContactCategoryAdmin)
