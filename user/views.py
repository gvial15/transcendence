from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from game.views import game

# Create your views here.

def login_form(request):
    if request.method == 'POST':
        username = request.POST['emailInput']
        password = request.POST['passwordInput']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return game(request) # redirect to game page
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')

def register_form(request):
    if request.method == 'POST':
        username = request.POST.get('emailInput')
        password = request.POST.get('registerPasswordInput')
        first_name = request.POST.get('firstNameInput')
        last_name = request.POST.get('lastNameInput')
        try:
            user = User.objects.create_user(username=username, email=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            return game(request) # redirect to game page
        except IntegrityError:
            messages.error(request, 'That email is already taken. Please choose another one.')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('/user/login')

def account(request):
    return render(request, 'account.html')