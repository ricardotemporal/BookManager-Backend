"""
This module sets up the main API using Django Ninja.

Classes and Functions:
- NinjaAPI: Creates and manages the API endpoints.
- add_router: Adds specific routes to the project.
  In this case, the "livros" router is linked to the "livros/" prefix.

Usage:
- The API can be accessed via the configured prefix (e.g., /livros/).
"""

from ninja import NinjaAPI
from livros.api import livros_router

# Create the main instance of the Ninja API
api = NinjaAPI()

# Add the router for book-related routes with the prefix "books/"
api.add_router('livros/', livros_router)
