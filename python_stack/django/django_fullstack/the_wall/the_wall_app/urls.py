from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='auth_home'),
    path('register', views.register, name='auth_register'),
    path('login', views.login, name='auth_login'),
    path('logout', views.logout, name='auth_logout'),
    path('check-email', views.check_email, name='check_email'),

    path('wall', views.wall_index, name='wall_index'),
    path('wall/post-message', views.create_message, name='post_message'),
    path('wall/post-comment', views.create_comment, name='post_comment'),
    path('wall/delete-message/<int:message_id>', views.delete_message, name='delete_message'),
]