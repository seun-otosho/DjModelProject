from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class ContactDetail(models.Model):
    """Generic Contact info """
    # Fields
    contact_info = models.CharField(max_length=30)

    # Relationships
    type = models.ForeignKey("contacts.ContactCategory", on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)

    # Fields
    object_id = models.PositiveIntegerField()
    contact_owner = GenericForeignKey("content_type", "object_id")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "contact_details"

    def __str__(self):
        return f"{self.contact_owner} <{self.contact_info}> {self.type} Contact info"

    def get_absolute_url(self):
        return reverse("contact_info_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("contact_info_update", args=(self.pk,))


class ContactCategory(models.Model):

    # Fields
    contact_type = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "contact_categories"
        verbose_name_plural = "Contact Categories"

    def __str__(self):
        return self.contact_type

    def get_absolute_url(self):
        return reverse("contact_category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("contact_category_update", args=(self.pk,))
