from django.urls import path
from .views import create_book_view, my_books_view, exchange_books_view

urlpatterns = [
    path('crear/', create_book_view, name='create_book'),
    path('mis-libros/', my_books_view, name='my_books'),
    path('intercambiar/', exchange_books_view, name='exchange_books'),


]
