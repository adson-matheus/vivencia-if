from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('esportes/horarios/', views.horarios, name='horarios'),
	path('esportes/reservas/sucesso', views.listar_reservas, name='listar_reservas'),
	path('esportes/reservar/<int:id>', views.realizar_reserva, name='realizar_reserva'),
	path('sobre/', views.sobre, name='sobre'),
]
