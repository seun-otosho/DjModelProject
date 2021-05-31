from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            "object_id",
            "content",
            "content_type",
            "parent",
        ]
