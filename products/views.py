import logging
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Product
from django.views.generic import ListView

# Configura el logger
logger = logging.getLogger(__name__)

class ProductsView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        product_count = queryset.count()
        print(f"[DEBUG] Se encontraron {product_count} productos en la base de datos.")
        logger.info(f"Productos cargados en vista: {product_count}")
        return queryset


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    logger.info(f"Intentando agregar producto al carrito: ID={product_id}, Usuario={request.user.username}")
    
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )

    if created:
        print(f"[DEBUG] Nuevo producto agregado al carrito: {product.name}")
        logger.info(f"Producto '{product.name}' agregado al carrito de {request.user.username}")
    else:
        cart_item.quantity += 1
        cart_item.save()
        print(f"[DEBUG] Cantidad incrementada para '{product.name}' en carrito")
        logger.info(f"Producto '{product.name}' actualizado en el carrito de {request.user.username} (Cantidad: {cart_item.quantity})")

    return redirect('cart:cart_view')
