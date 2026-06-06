from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books_index'),
    path('books/create', views.create_book, name='create_book'),
    path('books/<int:book_id>', views.show_book, name='show_book'),
    path('books/<int:book_id>/add_author', views.add_author_to_book, name='add_author_to_book'),
    
    path('authors', views.authors_index, name='authors_index'),
    path('authors/create', views.create_author, name='create_author'),
    path('authors/<int:author_id>', views.show_author, name='show_author'),
    path('authors/<int:author_id>/add_book', views.add_book_to_author, name='add_book_to_author'),
]