from rest_framework import viewsets, permissions

from . import serializers
from . import models


class StreetAddressViewSet(viewsets.ModelViewSet):
    """ViewSet for the StreetAddress class"""

    queryset = models.StreetAddress.objects.all()
    serializer_class = serializers.StreetAddressSerializer
    permission_classes = [permissions.IsAuthenticated]
