from django.contrib import admin
from django import forms

from . import models


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = "__all__"


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = [
        "last_updated",
        "content_object",
        "object_id",
        "created",
        "content",
    ]
    readonly_fields = [
        "last_updated",
        "content_object",
        "object_id",
        "created",
        "content",
    ]


admin.site.register(models.Comment, CommentAdmin)
