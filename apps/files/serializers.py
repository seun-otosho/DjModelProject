from rest_framework import serializers

from . import models


class submissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.submission
        fields = [
            "file_name",
            "last_updated",
            "file",
            "object_id",
            "created",
            "data_object",
        ]
