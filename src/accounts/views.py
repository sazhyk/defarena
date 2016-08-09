# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from userena.forms import SignupForm, AuthenticationForm
from django.contrib.auth.models import User


def home(request):
    context = {
        'login_form': AuthenticationForm
    }
    return render(request, 'home.html', context)


def register(request):
    context = {
        'signup_form': SignupForm
    }
    return render(request, 'register.html', context)
