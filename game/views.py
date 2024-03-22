from django.shortcuts import render

# Create your views here.
def game_menu(request) :
	return render(request, 'menu.html')