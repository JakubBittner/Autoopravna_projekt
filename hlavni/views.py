from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Kontrola, zda hesla odpovídají
        if password != confirm_password:
            messages.error(request, "Hesla se neshodují.")
            return redirect('register')

        # Kontrola, zda uživatelské jméno už není použito
        if User.objects.filter(username=username).exists():
            messages.error(request, "Toto uživatelské jméno je již obsazeno.")
            return redirect('register')

        # Kontrola, zda e-mail není již zaregistrovaný
        if User.objects.filter(email=email).exists():
            messages.error(request, "Tento e-mail je již zaregistrován.")
            return redirect('register')

        # Vytvoření uživatele
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Účet byl úspěšně vytvořen!")
        return redirect('login')  # Přejít na přihlašovací stránku nebo domovskou stránku

    return render(request, 'hlavni/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Snažíme se ověřit uživatele
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Pokud je uživatel validní, přihlásíme ho
            login(request, user)
            messages.success(request, "Úspěšně přihlášen!")
            return redirect('index')  # Přesměrujeme na hlavní stránku
        else:
            messages.error(request, "Neplatné přihlašovací údaje.")
            return redirect('login')  # Přesměrujeme zpět na přihlašovací stránku

    return render(request, 'hlavni/login.html')  # Vytvoř šablonu login.html


def index(request):
    return render(request, 'hlavni/index.html')
