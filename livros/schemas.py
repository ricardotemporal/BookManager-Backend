"""
This module defines schemas for handling and validating data in the API.

Schemas:
- LivroSchema: Used for creating or updating book data.
- LivrosViewSchema: Used for retrieving detailed book data, including the book's ID.
- AvaliacaoSchema: Used for handling book review data (rating and comments).
- FiltrosSortear: Defines filters for sorting or selecting books based on criteria.
"""

from ninja import ModelSchema, Schema
from .models import Livros

class LivroSchema(ModelSchema):
    """
    Schema for creating or updating book records.

    Fields:
    - nome: Name of the book.
    - streaming: Format of the book (physical or digital).
    """
    class Meta:
        model = Livros
        fields = ['nome', 'streaming']


class LivrosViewSchema(ModelSchema):
    """
    Schema for viewing book details.

    Fields:
    - nome: Name of the book.
    - streaming: Format of the book.
    - id: ID of the book.
    """
    class Meta:
        model = Livros
        fields = ['nome', 'streaming', 'id']


class AvaliacaoSchema(ModelSchema):
    """
    Schema for handling book reviews.

    Fields:
    - nota: Rating of the book.
    - comentarios: Comments or feedback on the book.
    """
    class Meta:
        model = Livros
        fields = ['nota', 'comentarios']


class FiltrosSortear(Schema):
    """
    Schema for filtering and sorting books.

    Fields:
    - nota_minima (int, optional): Minimum rating to filter books.
    - reler (bool, default=False): Whether to include books that have already been read.
    """
    nota_minima: int = None
    reler: bool = False
