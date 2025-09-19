from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', landing, name=''),
    path('signup', signup, name="signup"),
    path('login', auth_views.LoginView.as_view(template_name='Utilisateurs/login.html'), name='login'),
    path('logout', deconnection, name='logout'),
]