# -*- coding: utf-8 -*-
from django.shortcuts import render
from userena.forms import SignupForm, AuthenticationForm
from .forms import FileUploadForm


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


def new_capsule(request):

    form = FileUploadForm()

    context = {
        "form": form
    }

    return render(request, 'profile.html', context)
