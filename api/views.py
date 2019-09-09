from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import requests

def index(request):
	if not request.user.is_authenticated:
		return render(request, 'login.html')
	else:
		return render(request, 'index.html')

def logar(request):
	suapUrl='https://suap.ifrn.edu.br/api/v2/autenticacao/token/'
	matricula = ''
	senha=''
	if request.method =='POST':
		matricula = request.POST['username']
		senha = request.POST['password']
		try:
			requisicao = requests.post(suapUrl, data={'username': matricula, 'password': senha})
		except requests.exceptions.ConnectionError:
			return render(request, 'user/login.html', {'alerta2': 'Erro'})

		if 'token' in requisicao.text:

			user = authenticate(request,username=matricula, password=senha)
			if user is not None:
				login(request, user)
				return redirect('index')
				return HttpResponse('Autenticado')
			else:
				try:
					user = User.objects.get(username = matricula)
					if not user is None:
						user.set_password(senha)
						user.save()
				except:
					user = User.objects.create_user(username = matricula, password = senha)


				user = authenticate(request, username=matricula, password=senha)
				if user is not None:
					login(request, user)
					return redirect('index')
				else:
					return render(request, 'login.html')

				return redirect('index')


		else:
			return render(request, 'login.html', {'alerta': 'Erro'})


	else:
		return render(request, 'login.html')

def sair(request):
	logout(request)
	return render(request, 'login.html')
