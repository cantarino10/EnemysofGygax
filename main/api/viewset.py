from rest_framework import viewsets
from main.api import serializers
from main import models

class FeatsViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.FeatsSerializer
  queryset = models.Feats.objects.all()