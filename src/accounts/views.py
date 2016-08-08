# -*- coding: utf-8 -*-
from django.shortcuts import render
from userena.forms import SignupForm, AuthenticationForm


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
