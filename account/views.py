from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from verify_email.email_handler import send_verification_email


def signup(request):
    context = {}
    form = SignupForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        inactive_user = send_verification_email(request, form)
        user.save()

    context['form'] = form
    return render(request, 'registration/signup.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            if '@' in username:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    msg = 'Invalid credentials'
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    msg = 'Invalid credentials'

        else:
            msg = 'Error validating the form'

    return render(request, "registration/login.html", {"form": form, "msg": msg})
