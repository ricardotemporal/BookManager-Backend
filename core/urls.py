"""
This module defines the URL patterns for the Django project.

Paths:
- 'admin/': Provides access to the Django admin interface.
- 'api/': Maps to the endpoints defined in the Ninja API.

Usage:
- Add more paths here to define additional routes for the project.
"""

from django.contrib import admin
from django.urls import path
from .api import api

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the Django admin panel
    path('api/', api.urls),  # Route for the Ninja API endpoints
]
