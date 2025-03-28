from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # url para criar um novo usuário
    path('register/', views.UserCreateView.as_view(), name='register'),
    # URL para login
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # URL para logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]