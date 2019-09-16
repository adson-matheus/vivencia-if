from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm, NovoHorarioForm, EditarReservaForm

#pagina de sucesso na reserva 
def listar_reservas(request):
	reservas = Reserva.objects.all()
	return render(request, 'reserva_sucesso.html', {"reservas":reservas})

#aluno faz a reserva
def realizar_reserva(request, id):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		aluno = Reserva.objects.get(pk=id)
		if request.method=='POST':
			aluno = ReservaForm(request.POST, instance=aluno)
			if aluno.is_valid():
				aluno.save()
			return redirect('listar_reservas')
		else:
			aluno = ReservaForm(instance=aluno)
		return render(request, 'realizar_reserva.html', {'aluno':aluno})

#admin edita reserva se tiver algo errado
def editar_reserva(request, id):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		editar = Reserva.objects.get(pk=id)
		if request.method=='POST':
			editar = EditarReservaForm(request.POST, instance=editar)
			if editar.is_valid():
				editar.save()
			return redirect('horarios')
		else:
			editar = EditarReservaForm(instance=editar)
		return render(request, 'editar_reserva.html', {'editar':editar})

#admin exclui a reserva depois de uma semana para adicionar novas reservas.
def excluir_reserva(request, id):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		excluir = Reserva.objects.get(pk=id)
		excluir.delete()
		return redirect('horarios')

# Use as credenciais 'adson' e senha 'adson' para visualizar o lado do adm
def novo_horario(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		if not request.user.is_superuser:
			return redirect('index')
		else:
			if request.method=='POST':
				novo_horario = NovoHorarioForm(request.POST)
				if novo_horario.is_valid():
					obj = novo_horario.save(commit=False)
					obj.save()
					return redirect('horarios')
			else:
				novo_horario = NovoHorarioForm()
			return render(request, 'novo_horario.html', {'novo_horario':novo_horario})

#visualizar horarios disponiveis
def horarios(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		horarios = Reserva.objects.all()
		return render(request, 'horarios.html', {'horarios':horarios})

#sobre o projeto
def sobre(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		return render(request, 'sobre.html')