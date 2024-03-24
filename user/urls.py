from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.login_form),
	path('register/', views.register_form),
]