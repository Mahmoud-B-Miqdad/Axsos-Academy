from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='auth_home'),
    path('register', views.register, name='auth_register'),
    path('login', views.login, name='auth_login'),
    path('success', views.success, name='auth_success'),
    path('logout', views.logout, name='auth_logout'),
    path('check-email', views.check_email, name='check_email'),

    path('books', views.books_index, name='books_index'),
    path('books/add', views.add_book, name='add_book'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/update', views.update_book, name='update_book'),
    path('books/<int:book_id>/delete', views.delete_book, name='delete_book'),
    path('books/<int:book_id>/favorite/<str:action>', views.toggle_favorite, name='toggle_favorite'),
    path('favorites', views.my_favorites, name='my_favorites'),
]