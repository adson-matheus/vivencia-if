from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = ('aluno', 'esporte',)

class NovoHorarioForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = ('nome_professor', 'turno', 'horario', 'dia',)

class EditarReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = ('nome_professor', 'turno', 'horario', 'dia', 'esporte', 'aluno',)