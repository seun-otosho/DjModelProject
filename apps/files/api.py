from rest_framework import viewsets, permissions

from . import serializers
from . import models


class submissionViewSet(viewsets.ModelViewSet):
    """ViewSet for the submission class"""

    queryset = models.submission.objects.all()
    serializer_class = serializers.submissionSerializer
    permission_classes = [permissions.IsAuthenticated]
