from django import forms
from . import models


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = models.Institution
        fields = [
            "name",
            "date_re_registered",
            "date_licensed",
            "old_name",
            "ownership",
            "category",
        ]


class InstitutionCategoryForm(forms.ModelForm):
    class Meta:
        model = models.InstitutionCategory
        fields = [
            "institution_category",
        ]


class InstitutionOwnershipForm(forms.ModelForm):
    class Meta:
        model = models.InstitutionOwnership
        fields = [
            "institution_ownership",
        ]
