from rest_framework import serializers
from .models import Goals

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = ['id', 'title', 'description', 'target_date', 'status', 'created_at', 'updated_at']
