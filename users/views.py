from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
import requests
from statistics import mean

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')



@login_required
def ver_perfil_view(request, user_id):
    base_url = "http://localhost:8001"
    perfil, libros, solicitudes, historial, ratings = {}, [], [], [], []

    try:
        perfil_resp = requests.get(f"{base_url}/users/{user_id}")
        if perfil_resp.status_code == 200:
            perfil = perfil_resp.json()

        libros_resp = requests.get(f"{base_url}/books/user/{user_id}")
        if libros_resp.status_code == 200:
            libros = libros_resp.json()

        solicitudes_resp = requests.get(f"{base_url}/exchange-requests/received/{user_id}")
        if solicitudes_resp.status_code == 200:
            solicitudes = solicitudes_resp.json()

        historial_resp = requests.get(f"{base_url}/history/user/{user_id}")
        if historial_resp.status_code == 200:
            historial = historial_resp.json()

        ratings_resp = requests.get(f"{base_url}/ratings/user/{user_id}")
        if ratings_resp.status_code == 200:
            ratings = ratings_resp.json()

        print("📌 Perfil:", perfil)
        print("📘 Libros:", libros)
        print("📩 Solicitudes:", solicitudes)
        print("🔁 Historial:", historial)
        print("⭐ Ratings:", ratings)

    except Exception as e:
        print("❌ Error al conectar con la API:", e)

    return render(request, "users/profile.html", {
        "perfil": perfil,
        "libros": libros,
        "solicitudes": solicitudes,
        "historial": historial,
        "ratings": ratings,
    })
