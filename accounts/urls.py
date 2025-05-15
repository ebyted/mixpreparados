from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_redirect, register_view, register_redirect

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login-redirect/', login_redirect, name='login_redirect'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register_view, name='register'),
    path('register-redirect/', register_redirect, name='register_redirect'),
]
