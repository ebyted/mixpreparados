from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required 
def register_redirect(request):
    return render(request, "registration/register_redirect.html")

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático tras registro
            return redirect('accounts:register_redirect') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def login_redirect(request):
    return render(request, 'registration/login_redirect.html')

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session.modified = True
        return redirect('accounts:login_redirect')