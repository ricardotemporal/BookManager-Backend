"""
This module registers the models with the Django admin interface.

Models:
- Livros: Represents the books themselves.

Usage:
- The "Livros" model will be available for management in the Django admin panel.
"""

from django.contrib import admin
from .models import Livros

# Registering the "Livros" model in the Django admin interface
admin.site.register(Livros)  # Enables management of books
