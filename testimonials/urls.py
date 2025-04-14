from django.urls import path
from .views import testimonios_view  # <-- asegúrate de importar esta vista

urlpatterns = [
    path('', testimonios_view, name='testimonials'),  # <-- Aquí cambiamos a la función que renderiza el formulario
]