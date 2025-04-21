from datetime import timedelta
from django.utils import timezone
from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

# This function will be called when a new Task is created
def get_due_date_default():
    """
    Returns a default due date 7 days from now.
    Used as the default value for the 'due_date' field.
    """
    return timezone.now() + timedelta(days=7)
# Create your models here.

class Task(models.Model):
    """
    Represents a task created by a user.

    Features:
    - Owned by a user (owner)
    - Can be assigned to another user (assigned_to)
    - Includes due date, completion status, and timestamps
    """
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,help_text="Hello Title of the task (min 3 characters)")
    description = models.TextField(blank=True)
    # ✅ New fields for filtering and management
    is_completed = models.BooleanField(default=False)  # Boolean with default
    due_date = models.DateField(default=get_due_date_default, null=True, blank=True,help_text="Due date must be today or in the future")  # Optional date
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tasks',
        on_delete=models.CASCADE
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the task.
        """
        return self.title
    
