from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'full_name', 'password']  
        extra_kwargs = {
            'password': {'write_only': True},
        }
        def create(self, validated_data):
        # Extract fields from validated data
            email = validated_data.get('email')
            username = validated_data.get('username')
            full_name = validated_data.get('full_name')
            password = validated_data.get('password')

            # Create user using create_user to hash the password
            user = User.objects.create_user(
                email=email,
                username=username,
                full_name=full_name,
                password=password  # password is hashed here
            )
            return user