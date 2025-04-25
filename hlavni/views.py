from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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

        # Vytvoření uživatele
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Účet byl úspěšně vytvořen!")
        return redirect('login')  # Přejít na přihlašovací stránku nebo domovskou stránku

    return render(request, 'hlavni/register.html')


def register(request):
    return render(request, 'hlavni/register.html')

def index(request):
    return render(request, 'hlavni/index.html')
