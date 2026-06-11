from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/destroy/', views.destroy_course, name='destroy_course'),
    path('courses/<int:course_id>/comments/', views.course_comments, name='course_comments'),
    
    # AJAX Endpoint for Sensei Bonus
    path('courses/<int:course_id>/delete-ajax/', views.delete_course_ajax, name='delete_course_ajax'),
]