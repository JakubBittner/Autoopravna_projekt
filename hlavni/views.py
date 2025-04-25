from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

        messages.success(request, "Účet byl úspěšně vytvořen!")
        return redirect('login')

    return render(request, 'hlavni/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Úspěšně přihlášen!")
            return redirect('dashboard')
        else:
            messages.error(request, "Neplatné přihlašovací údaje.")
            return redirect('login')

    return render(request, 'hlavni/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, 'hlavni/index.html')


def dashboard(request):
    return render(request, 'hlavni/dashboard.html')
