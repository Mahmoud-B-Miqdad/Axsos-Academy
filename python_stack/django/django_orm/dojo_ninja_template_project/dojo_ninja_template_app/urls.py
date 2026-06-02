from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.create_dojo),
    path('add_ninja', views.create_ninja),
    path('delete_dojo/<int:dojo_id>', views.delete_dojo), 
]