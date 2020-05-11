from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import RegForm
from django.views.generic import CreateView
from .models import XxUser

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'userapp/login.html'

class UserCreateView(CreateView):
    model = XxUser
    template_name = 'userapp/register.html'
    form_class = RegForm
    success_url = reverse_lazy('users:login')