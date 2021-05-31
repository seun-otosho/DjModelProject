from rest_framework import serializers

from . import models


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Institution
        fields = [
            "last_updated",
            "name",
            "created",
            "date_re_registered",
            "date_licensed",
            "old_name",
        ]

class InstitutionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InstitutionCategory
        fields = [
            "created",
            "institution_category",
            "last_updated",
        ]

class InstitutionOwnershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InstitutionOwnership
        fields = [
            "created",
            "last_updated",
            "institution_ownership",
        ]
