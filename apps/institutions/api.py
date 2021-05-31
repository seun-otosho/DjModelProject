from rest_framework import viewsets, permissions

from . import serializers
from . import models


class InstitutionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Institution class"""

    queryset = models.Institution.objects.all()
    serializer_class = serializers.InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstitutionCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the InstitutionCategory class"""

    queryset = models.InstitutionCategory.objects.all()
    serializer_class = serializers.InstitutionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class InstitutionOwnershipViewSet(viewsets.ModelViewSet):
    """ViewSet for the InstitutionOwnership class"""

    queryset = models.InstitutionOwnership.objects.all()
    serializer_class = serializers.InstitutionOwnershipSerializer
    permission_classes = [permissions.IsAuthenticated]
