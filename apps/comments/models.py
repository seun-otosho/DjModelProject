from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class Comment(models.Model):
    """Generic Comments for objects with self parental functionality"""
    content = models.TextField(max_length=128)
    # Relationships
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent = models.ForeignKey("comments.Comment", on_delete=models.PROTECT)

    # Fields
    content_object = GenericForeignKey("content_type", "object_id")
    object_id = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("comment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("comment_update", args=(self.pk,))
