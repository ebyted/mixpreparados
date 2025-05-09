from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Product  # Asegúrate de tener esto también
from django.views.generic import ListView

class ProductsView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = 'products'

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Intenta encontrar el CartItem existente para ese usuario y producto
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )

    # Si ya existe, solo aumenta la cantidad
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_view')