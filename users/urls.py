from django.urls import path
from .views import UserRegisterView,UserListView,UserDetailView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('', UserListView.as_view(), name='user-list'),  # New GET endpoint
]