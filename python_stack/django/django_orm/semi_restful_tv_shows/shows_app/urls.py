from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all_shows'),                          # GET - Display the entire table/list of shows
    path('new', views.new, name='new_show'),                          # GET - Display the form to add a new show
    path('create', views.create, name='create_show'),                 # POST - Process the form submission to add a new show
    path('<int:show_id>', views.show, name='show_detail'),            # GET - Display details for a specific show
    path('<int:show_id>/edit', views.edit, name='edit_show'),         # GET - Display the form to edit an existing show's data
    path('<int:show_id>/update', views.update, name='update_show'),   # POST - Process the data update for a specific show
    path('<int:show_id>/destroy', views.destroy, name='delete_show'), # POST/GET - Delete a specific show from the database
]