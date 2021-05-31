from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Comment class"""

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
