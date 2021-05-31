from rest_framework import serializers

from . import models


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = [
            "last_updated",
            "content_object",
            "object_id",
            "created",
            "content",
        ]
