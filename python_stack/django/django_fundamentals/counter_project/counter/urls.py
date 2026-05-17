from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('plus_two', views.plus_two),
    path('custom_increment', views.custom_increment),
    path('destroy_session', views.destroy_session),
    path('reset', views.reset),

]