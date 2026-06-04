from django.shortcuts import render

from rest_framework import viewsets
from .models import Goals
from .serializers import GoalSerializer

class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goals.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




