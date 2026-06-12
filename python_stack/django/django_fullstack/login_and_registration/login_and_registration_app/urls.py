from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='auth_home'),
    path('register', views.register, name='auth_register'),
    path('login', views.login, name='auth_login'),
    path('success', views.success, name='auth_success'),
    path('logout', views.logout, name='auth_logout'),
    path('check-email', views.check_email, name='check_email'),
]