from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Hlavní stránka
    path('register/', views.register, name='register'),  # Stránka pro registraci
    path('login/', views.login_view, name='login'),  # Stránka pro přihlášení
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),  # Profilová stránka
]
