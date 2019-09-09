from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.index, name='login'),
    path('entrando/', views.logar, name='logar'),
    path('logout/', views.sair, name='sair'),
]
