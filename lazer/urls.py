from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('esportes/horarios/', views.horarios, name='horarios'),
	path('esportes/reservas/sucesso', views.listar_reservas, name='listar_reservas'),
	path('esportes/reservar/<int:id>', views.realizar_reserva, name='realizar_reserva'),
	path('sobre/', views.sobre, name='sobre'),
	#admin
	path('add/horario', views.novo_horario, name='novo_horario'),
	path('editar/reserva/<int:id>', views.editar_reserva, name='editar_reserva'),
	path('excluir/reserva/<int:id>', views.excluir_reserva, name='excluir_reserva'),
]
