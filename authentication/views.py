from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from game.views import game_menu

# Create your views here.

def	login_form(request) :
	if request.method == 'POST':
		username = request.POST['emailInput']
		password = request.POST['passwordInput']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return game_menu(request) # redirect to game page
		else:
			return render(request, 'login.html', {'error': 'Invalid credentials'})
	return render(request, 'login.html')

def	register_form(request) :
	if request.method == 'POST':
		username = request.POST['emailInput']  # Use email as username or adjust accordingly
		password = request.POST['registerPasswordInput']
		user = User.objects.create_user(username=username, password=password)
		user.first_name = request.POST['firstNameInput']
		user.last_name = request.POST['lastNameInput']
		user.save()
		login(request, user)
		return game_menu(request) # redirect to game page
	return render(request, 'register.html')
