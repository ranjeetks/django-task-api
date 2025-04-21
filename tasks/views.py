from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError

import logging
logger = logging.getLogger('task')

class TaskPagination(PageNumberPagination):
    page_size = 5

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authenticated users to manage their tasks.

    Features:
    - Users can create, retrieve, update, and delete their own tasks.
    - Supports filtering by completion status and due date.
    - Supports search by task title and description.
    - Includes pagination for task lists.
    - Tasks are created with the current user as the owner.
    - Optionally, tasks can be assigned to other users.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = TaskPagination  # 🔄 Custom pagination class
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # Filter by completion status & due_date
    filterset_fields = ['is_completed', 'due_date']
    
    # 🔍 Search by title and description
    search_fields = ['title', 'description']

    
    

    def perform_create(self, serializer):
        """
        Automatically assigns the current user as the task owner when creating a task.
        """
        try:
            task=serializer.save(owner=self.request.user)  # 🔥 This sets the owner
            logger.info(f"Task created by {self.request.user.email} - Task ID: {task.id}")
        except Exception as e:
            logger.error(f"Error while creating task for user {self.request.user.email}: {str(e)}", exc_info=True)
            raise ValidationError(f"Failed to create task: {str(e)}")
    
    def get_queryset(self):
        """
        Restricts the task list to the authenticated user's tasks only.
        """
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(owner=user)
        return Task.objects.none()  # Return empty queryset if anonymous
    
    @extend_schema(
        # operation_description="Retrieve a paginated list of tasks for the authenticated user. "
        #                       "Supports filtering by 'is_completed' and 'due_date', "
        #                       "and searching by title/description.",
        parameters=[
            OpenApiParameter(name='page', type=int, description='Page number'),
            OpenApiParameter(name='is_completed', type=bool, description='Filter by completion status'),
            OpenApiParameter(name='due_date', type=str, description='Filter by due date'),
            OpenApiParameter(name='search', type=str, description='Search by title or description'),
        ]
    )
    def list(self, request, *args, **kwargs):
        """
        Returns a list of tasks belonging to the authenticated user,
        with optional search, filters, and pagination.
        """
        return super().list(request, *args, **kwargs)