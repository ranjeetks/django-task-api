from rest_framework import serializers
from .models import Task
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()

class UserShortSerializer(serializers.ModelSerializer):
    """
    Short serializer to display basic user info for 'assigned_to' field.
    """
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model. Handles task creation, update, validation,
    and nested user assignment display.

    Features:
    - Displays owner username as 'owner_name'
    - Handles assignment using 'assigned_to_id'
    - Validates title length and due date
    """
    owner_name = serializers.CharField(source='owner.username', read_only=True)  # Add this line to show owner's username
    assigned_to = UserShortSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, source='assigned_to'
    )
    class Meta:
        model = Task
        #fields = ['id', 'title', 'description', 'owner_name']  # Include 'owner_name' instead of 'owner'
        fields='__all__'
        read_only_fields = ['owner']  # Keep 'owner' field as read-only (so it won't be required in the request)
# ✅ Validate title is not empty or too short
    def validate_title(self, value):
        """
        Ensure the title is not empty or too short.
        """
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
        # ✅ Validate due_date is not in the past
    def validate_due_date(self, value):
        """
        Ensure the due date is today or in the future.
        """
        if value and value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value