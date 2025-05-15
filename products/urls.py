from django.urls import path
from .views import add_to_cart, ProductsView

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),  # Página dinámica de productos
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart_from_products'),  # Agregar al carrito
]


