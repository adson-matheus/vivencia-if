from django.db import models
from model_utils import Choices

class Reserva(models.Model):
	opcoes_turno = Choices(('Manhã', 'Manhã'),
							('Tarde', 'Tarde'),
							('Noite', 'Noite'),)

	opcoes_dia = Choices(('Segunda', 'Segunda'),
						('Terça', 'Terça'),
						('Quarta', 'Quarta'),
						('Quinta', 'Quinta'),
						('Sexta', 'Sexta'),)
	opcoes_professor = Choices(('Ari Oliveira', 'Ari Oliveira'),
								('Mariana', 'Mariana'),
								('Romerito', 'Romerito'),
								('Hudson', 'Hudson'),)
	opcoes_esporte = Choices(('Futebol', 'Futebol'),
							('Futsal', 'Futsal'),
							('Vôlei', 'Vôlei'),
							('Basquete', 'Basquete'),
							('Badminton', 'Badminton'),
							('Natação', 'Natação'),)
	nome_professor = models.CharField('Nome do professor', choices=opcoes_professor, default=opcoes_professor.Romerito, max_length=40)
	turno = models.CharField('Turno', max_length=5, choices=opcoes_turno, default=opcoes_turno.Manhã)
	horario = models.CharField('Horário', max_length=20)
	dia = models.CharField('Dia disponível', choices=opcoes_dia, max_length=20, default=opcoes_dia.Segunda)
	aluno = models.IntegerField(blank=True, null=True)
	esporte = models.CharField(max_length=20, choices=opcoes_esporte, blank=True, null=True)
