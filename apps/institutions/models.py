from django.db import models
from django.urls import reverse


class Institution(models.Model):
    # Fields
    name = models.CharField(max_length=64)
    date_re_registered = models.DateField()
    date_licensed = models.DateField()
    old_name = models.CharField(max_length=64)

    # Relationships
    ownership = models.ForeignKey("institutions.InstitutionOwnership", on_delete=models.PROTECT)
    category = models.ForeignKey("institutions.InstitutionCategory", on_delete=models.PROTECT)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "institutions"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("institution_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("institution_update", args=(self.pk,))


class InstitutionCategory(models.Model):

    # Fields
    institution_category = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "institution_categories"
        verbose_name = "Institution Category"

    def __str__(self):
        return self.institution_category

    def get_absolute_url(self):
        return reverse("institution_category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("institution_category_update", args=(self.pk,))


class InstitutionOwnership(models.Model):

    # Fields
    institution_ownership = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "institution_ownerships"

    def __str__(self):
        return self.institution_ownership

    def get_absolute_url(self):
        return reverse("institution_ownership_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("institution_ownership_update", args=(self.pk,))
