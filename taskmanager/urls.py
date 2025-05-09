"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import permissions
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
#from django.http import JsonResponse
from django.http import HttpResponse


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Task Management API",
#       default_version='v1',
#       description="API documentation for your Task Management app",
#       contact=openapi.Contact(email="testuser@example.com"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
#    authentication_classes=[]  # ✅ Optional but safe to keep
# )

def root_view(request):
    return HttpResponse("Welcome to the Task Manager API!")
    #return JsonResponse({"message": "Welcome to the Task Management API!", "docs": "/api/docs/"})

urlpatterns = [
    path('api/', root_view),  # 👈 Add this
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api/users/', include('users.urls')),

    # Swagger documentation
    #re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Schema JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
