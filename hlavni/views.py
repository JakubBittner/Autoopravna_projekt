from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Hesla se neshodují.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Toto uživatelské jméno je již obsazeno.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Tento e-mail je již zaregistrován.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Účet byl úspěšně vytvořen! Nyní se můžete přihlásit.")
        return redirect('login')

    return render(request, 'hlavni/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Úspěšně přihlášen!")
            # redirect podle role – jména URL z urls.py, viz níže
            if user.is_superuser:
                return redirect('admin_dashboard')   # name='admin_dashboard'
            else:
                return redirect('dashboard')         # name='dashboard'
        else:
            messages.error(request, "Neplatné přihlašovací údaje.")
            return redirect('login')                # name='login'

    return render(request, 'hlavni/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Úspěšně odhlášen!")
    return redirect('index')                          # name='index'


def index(request):
    return render(request, 'hlavni/index.html')


@login_required(login_url='login')                    # name='login'
def dashboard(request):
    return render(request, 'hlavni/dashboard.html')


@login_required(login_url='login')
def profile(request):
    return render(request, 'hlavni/dashboard.html')


@login_required(login_url='login')
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, "Nemáte přístup na tuto stránku.")
        return redirect('dashboard')
    return render(request, 'hlavni/admin_dashboard.html')
