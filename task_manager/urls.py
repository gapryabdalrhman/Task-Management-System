from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger Documentation Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="API for managing tasks",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@taskmanager.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('swagger/', schema_view.as_view(), name='swagger'),
    # JWT Authentication Endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # Get access & refresh tokens
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh access token
]
