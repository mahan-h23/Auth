from django.shortcuts import render
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
    return render(request,'registration/signup.html',context)


def login_view(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'registration/login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page?
            # return HttpResponseRedirect('/')
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'registration/login.html', {'context': context})