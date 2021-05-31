from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ContactDetailViewSet(viewsets.ModelViewSet):
    """ViewSet for the ContactDetail class"""

    queryset = models.ContactDetail.objects.all()
    serializer_class = serializers.ContactDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the ContactCategory class"""

    queryset = models.ContactCategory.objects.all()
    serializer_class = serializers.ContactCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
