from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegisterForm


def get_user_role(user):
    profile = getattr(user, 'profile', None)
    if profile is None:
        return 'User'

    role = profile.role
    if role == 'moderator':
        return 'Moderator'
    if role == 'admin':
        return 'Administrator'
    return 'User'


def home(request):
    return render(request, 'GroupPortal/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'GroupPortal/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'GroupPortal/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    role = get_user_role(request.user)

    return render(request, 'GroupPortal/dashboard.html', {
        'user': request.user,
        'role': role,
    })
