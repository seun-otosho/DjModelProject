from django.contrib import admin
from django import forms
from django.http import request
from django.shortcuts import render
from django.urls import path

from . import models


class InstitutionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Institution
        fields = "__all__"


class InstitutionAdmin(admin.ModelAdmin):
    form = InstitutionAdminForm
    list_display = [
        "name",
        "date_licensed",
        "date_re_registered",
        "old_name",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]

    change_list_template = "institutions/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('upload-institutions/', self.upload_institutions),]
        return my_urls + urls

    def upload_institutions(self, request):
        # form = CsvImportForm()
        payload = {} # "form": form
        return render(
            request, "institutions/data_import_form.html", payload
        )


class InstitutionCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.InstitutionCategory
        fields = "__all__"


class InstitutionCategoryAdmin(admin.ModelAdmin):
    form = InstitutionCategoryAdminForm
    list_display = [
        "institution_category",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "institution_category",
        "created",
        "last_updated",
    ]


class InstitutionOwnershipAdminForm(forms.ModelForm):

    class Meta:
        model = models.InstitutionOwnership
        fields = "__all__"


class InstitutionOwnershipAdmin(admin.ModelAdmin):
    form = InstitutionOwnershipAdminForm
    list_display = [
        "institution_ownership",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "institution_ownership",
        "created",
        "last_updated",
    ]


admin.site.register(models.Institution, InstitutionAdmin)
admin.site.register(models.InstitutionCategory, InstitutionCategoryAdmin)
admin.site.register(models.InstitutionOwnership, InstitutionOwnershipAdmin)
