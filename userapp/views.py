from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from .forms import RegForm
from django.views.generic import CreateView, DetailView
from .models import XxUser
from rest_framework.authtoken.models import Token

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'userapp/login.html'

class UserCreateView(CreateView):
    model = XxUser
    template_name = 'userapp/register.html'
    form_class = RegForm
    success_url = reverse_lazy('users:login')

class UserDetailView(DetailView):
    template_name = 'userapp/profile.html'
    model = XxUser


def update_token(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        # создать
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))

def create_token(request):
    user = request.user
    Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))

def update_token_ajax(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        token = Token.objects.create(user=user)
    else:
        # создать
        token = Token.objects.create(user=user)
    return JsonResponse({'key': token.key})