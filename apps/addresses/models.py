from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class StreetAddress(models.Model):
    """Generic Addresses for objects"""
    # Fields
    street_address = models.TextField(max_length=100)
    area = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    # Relationships
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    address_owner = GenericForeignKey("content_type", "object_id")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("addresses_StreetAddress_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("addresses_StreetAddress_update", args=(self.pk,))
