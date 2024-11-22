"""
This module defines the database models for the application.

Models:
- Livros: Represents books with details like name, format (physical or digital), rating, and comments.
"""

from django.db import models


class Livros(models.Model):
    """
    Represents a book with various attributes.

    Fields:
    - nome (CharField): The name of the book (maximum 50 characters).
    - streaming (CharField): The format of the book (physical or digital).
      Choices:
        - 'F': Physical
        - 'AK': Amazon Kindle
    - nota (IntegerField): The rating of the book (nullable).
    - comentarios (TextField): Comments or reviews about the book (nullable).
    """
    streaming_choices = (('F', 'Physical'), ('AK', 'Amazon Kindle'))
    nome = models.CharField(max_length=50)
    streaming = models.CharField(max_length=2, choices=streaming_choices)
    nota = models.IntegerField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the book.
        """
        return self.nome
