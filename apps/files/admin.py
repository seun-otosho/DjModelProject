from django.contrib import admin
from django import forms

from . import models


class SubmissionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Submission
        fields = "__all__"


class SubmissionAdmin(admin.ModelAdmin):
    form = SubmissionAdminForm
    list_display = [
        "file_name",
        "file",
        "data_object",
        # "object_id",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "file_name",
        # "file",
        # "object_id",
        # "data_object",
        "created",
        "last_updated",
    ]


admin.site.register(models.Submission, SubmissionAdmin)
