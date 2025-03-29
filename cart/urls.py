from django.urls import path
from . import views

app_name = 'cart'  # 👈 Esto es clave para el namespace

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
]