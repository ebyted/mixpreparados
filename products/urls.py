from django.urls import path
from .views import add_to_cart, ProductsStaticView  # 👈 solo importa tus vistas de products

app_name = 'products'  # define el namespace para esta app

urlpatterns = [
    path('', ProductsStaticView.as_view(), name='products'),  # Página de productos
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart_from_products'),# Ruta para agregar al carrito
]
