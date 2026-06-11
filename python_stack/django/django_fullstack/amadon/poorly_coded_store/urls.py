from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy_product, name='buy_product'),  # POST route only
    path('checkout/', views.checkout, name='checkout'),   # GET route for thank you page
]