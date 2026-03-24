"""
URL configuration for scr_project_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('assignments/', views.assignments, name='assignments'),
    path('players/', views.players, name='players'),
    path('units/', views.units, name='units'),
    path('assignments/<int:id>/delete/', views.delete_assignment, name='delete_assignment'),
    path('players/<str:username>/delete/', views.delete_player, name='delete_player'),
    path('units/<int:id>/delete/', views.delete_unit, name='delete_unit'),
    path('create_player/', views.create_player, name='create_player'),
    path('create_assignment/', views.create_assignment, name='create_assignment'),
    path('create_unit/', views.create_unit, name='create_unit'),
]