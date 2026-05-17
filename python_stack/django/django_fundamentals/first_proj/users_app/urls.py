from django.urls import path
from . import views
from blogs_app import views as blog_views 

urlpatterns = [
    path('', blog_views.index), 

    path('register', views.register),   
    path('login', views.login),         
    path('users/new', views.register),  
    path('users', views.index),         
]