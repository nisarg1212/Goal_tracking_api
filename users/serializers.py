from rest_framework import serializers
from .models import CustomUser

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validate_data):
        user = CustomUser.objects.create_user(
            username=validate_data['username'],
            email = validate_data['email'],
            first_name = validate_data['first_name', ''],
            last_name = validate_data['last_name', ''],
            password = validate_data['password']
            )
        return user