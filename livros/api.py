"""
This module defines the routes for managing books and their interactions using Ninja Router.

Routes:
- GET `/`: Retrieves a list of all books.
- POST `/`: Creates a new book with the provided details.
- PUT `/{livro_id}`: Adds a review to a book, including comments and a rating.
- DELETE `/{livro_id}`: Deletes a book by its ID.
- GET `/sortear/`: Retrieves a random book based on optional filters (rating and re-read status).

Schemas:
- LivroSchema: Defines the structure for book-related data.
- AvaliacaoSchema: Defines the structure for review-related data.
- FiltrosSortear: Filters used for sorting a book randomly.
- LivrosViewSchema: Used to structure book view responses.

Models:
- Livros: Represents the books.

Usage:
- Use these routes to perform CRUD operations on books and manage their data.
"""

from ninja import Router, Query
from .models import Livros
from .schemas import LivroSchema, AvaliacaoSchema, FiltrosSortear, LivrosViewSchema
from typing import List

livros_router = Router()

@livros_router.get('/', response={200: List[LivrosViewSchema]})
def get_livro(request):
    """
    Retrieve all books.
    """
    livros = Livros.objects.all()
    return livros

@livros_router.post('/', response={200: LivroSchema})
def create_livro(request, livro_schema: LivroSchema):
    """
    Create a new book.

    Args:
    - livro_schema (LivroSchema): Schema containing book details.
    """
    nome = livro_schema.dict()['nome']
    streaming = livro_schema.dict()['streaming']
    livro = Livros(nome=nome, streaming=streaming)
    livro.save()
    return livro

@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id: int, avaliacao_schema: AvaliacaoSchema):
    """
    Add a review to a book.

    Args:
    - livro_id (int): ID of the book.
    - avaliacao_schema (AvaliacaoSchema): Schema containing review details.
    """
    comentarios = avaliacao_schema.dict()['comentarios']
    nota = avaliacao_schema.dict()['nota']
    livro = Livros.objects.get(id=livro_id)
    livro.comentarios = comentarios
    livro.nota = nota
    livro.save()
    return {'status': 'Review added successfully'}

@livros_router.delete('/{livro_id}')
def deletar_livro(request, livro_id: int):
    """
    Delete a book by ID.

    Args:
    - livro_id (int): ID of the book to delete.
    """
    livro = Livros.objects.get(id=livro_id)
    livro.delete()
    return livro_id

@livros_router.get('/sortear/', response={200: LivroSchema, 404: dict})
def sortear_livro(request, filtros: Query[FiltrosSortear]):
    """
    Retrieve a random book based on filters.

    Args:
    - filtros (Query[FiltrosSortear]): Query parameters for filtering books.
    """
    nota_minima = filtros.dict()['nota_minima']
    reler = filtros.dict()['reler']
    livros = Livros.objects.all()
    if not reler:
        livros = livros.filter(nota=None)
    if nota_minima:
        livros = livros.filter(nota__gte=nota_minima)
    livro = livros.order_by('?').first()
    if livros.count() > 0:
        return 200, livro
    else:
        return 404, {'status': 'Book not found'}
