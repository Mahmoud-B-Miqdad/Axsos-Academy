from django.urls import path
from . import views

urlpatterns = [
    # Root redirect to /shows
    path('', views.root_redirect, name='root_redirect'),
    
    # Read All Shows
    path('shows/', views.index, name='all_shows'),
    
    # Render New Show Form
    path('shows/new/', views.new_show, name='new_show'),
    
    # Process Creation Form
    path('shows/create/', views.create_show, name='create_show'),
    
    # Read One Specific Show
    path('shows/<int:show_id>/', views.show_detail, name='show_detail'),
    
    # Render Edit Show Form
    path('shows/<int:show_id>/edit/', views.edit_show, name='edit_show'),
    
    # Process Update Form
    path('shows/<int:show_id>/update/', views.update_show, name='update_show'),
    
    # Process Delete Action
    path('shows/<int:show_id>/destroy/', views.destroy_show, name='destroy_show'),
    
    # AJAX Live Validation Endpoint (Sensei Bonus)
    path('shows/validate-ajax/', views.validate_ajax, name='validate_ajax'),
]