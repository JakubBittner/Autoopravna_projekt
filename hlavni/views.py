from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Repair, RepairReservation, Auto
from .forms import RepairForm, RepairReservationForm, AutoForm

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
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, "Neplatné přihlašovací údaje.")
            return redirect('login')

    return render(request, 'hlavni/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Úspěšně odhlášen!")
    return redirect('index')


def index(request):
    return render(request, 'hlavni/index.html')


@login_required(login_url='login')
def dashboard(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')

    repairs = Repair.objects.filter(customer=request.user)
    reservations = RepairReservation.objects.filter(user=request.user)
    return render(request, 'hlavni/dashboard.html', {
        'repairs': repairs,
        'reservations': reservations
    })


@login_required(login_url='login')
def profile(request):
    return render(request, 'hlavni/dashboard.html')


@login_required(login_url='login')
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, "Nemáte přístup na tuto stránku.")
        return redirect('dashboard')

    if request.method == "POST":
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Oprava byla úspěšně přidána.")
            return redirect('admin_dashboard')
    else:
        form = RepairForm()

    repairs = Repair.objects.all()

    return render(request, 'hlavni/admin_dashboard.html', {'form': form, 'repairs': repairs})


@login_required
def reservation_view(request):
    if request.method == 'POST':
        form = RepairReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('dashboard')
    else:
        form = RepairReservationForm()

    return render(request, 'hlavni/reservation.html', {'form': form})


@login_required
def reservation_success(request):
    return render(request, 'hlavni/reservation_success.html')

@login_required(login_url='login')
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, "Nemáte přístup na tuto stránku.")
        return redirect('dashboard')

    repair_form = RepairForm()
    auto_form = AutoForm()

    if request.method == "POST":
        if 'oprava-submit' in request.POST:
            repair_form = RepairForm(request.POST)
            if repair_form.is_valid():
                repair_form.save()
                messages.success(request, "Oprava byla úspěšně přidána.")
                return redirect('admin_dashboard')

        elif 'auto-submit' in request.POST:
            auto_form = AutoForm(request.POST)
            if auto_form.is_valid():
                auto_form.save()
                messages.success(request, "Auto bylo úspěšně přidáno do půjčovny.")
                return redirect('admin_dashboard')

    repairs = Repair.objects.all()
    auta = Auto.objects.all()

    return render(request, 'hlavni/admin_dashboard.html', {
        'form': repair_form,
        'auto_form': auto_form,
        'repairs': repairs,
        'auta': auta,
    })