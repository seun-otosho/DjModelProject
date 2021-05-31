from rest_framework import serializers

from . import models


class StreetAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StreetAddress
        fields = [
            "street_address",
            "state",
            "country",
            "area",
            "last_updated",
            "object_id",
            "created",
            "address_owner",
        ]
