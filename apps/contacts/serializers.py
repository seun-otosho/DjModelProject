from rest_framework import serializers

from . import models


class ContactDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactDetail
        fields = [
            "object_id",
            "contact_owner",
            "contact_info",
            "last_updated",
            "created",
        ]

class ContactCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactCategory
        fields = [
            "last_updated",
            "contact_type",
            "created",
        ]
