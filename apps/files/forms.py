from django import forms
from . import models


class submissionForm(forms.ModelForm):
    class Meta:
        model = models.submission
        fields = [
            "file_name",
            "file",
            "object_id",
            "content_type",
        ]
