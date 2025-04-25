from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Hlavní stránka
    path('register/', views.register, name='register'),  # Stránka pro registraci
    path('login/', views.login_view, name='login'),  # Stránka pro přihlášení (pokud ji chceš přidat)
]
