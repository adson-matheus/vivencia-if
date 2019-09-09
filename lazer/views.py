from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm

# def esportes(request):
# 	if not request.user.is_authenticated:
# 		return redirect('login')
# 	else:
# 		return render(request, 'esportes.html')

def horarios(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		horarios = Reserva.objects.all()
		return render(request, 'horarios.html', {'horarios':horarios})

def listar_reservas(request):
	reservas = Reserva.objects.all()
	return render(request, 'reserva_sucesso.html', {"reservas":reservas})

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

def sobre(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		return render(request, 'sobre.html')