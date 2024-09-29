# myapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para la página de inicio
    path('register/', views.register, name='register'),  # URL para registro
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),  # Corrige el login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Corrige el logout
    path('item/new/', views.item_create, name='item_create'),  # Crear nuevo item
    path('item/edit/<int:pk>/', views.item_edit, name='item_edit'),  # Editar item
    path('item/delete/<int:pk>/', views.item_delete, name='item_delete'),  # Eliminar item
]
