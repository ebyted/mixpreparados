from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Asegúrate de tener definida esta ruta
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})