from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class Submission(models.Model):

    # Fields
    file_name = models.CharField(max_length=64)
    file = models.FileField(upload_to="upload/files/")
    # Relationships
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    data_object = GenericForeignKey("content_type", "object_id")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "submissions"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("file_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("file_update", args=(self.pk,))
