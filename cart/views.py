import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem
from products.models import Product

# Vista principal del carrito
@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in items)
    return render(request, 'static_templates/cart/cart.html', {
        'cart_items': items,
        'total': total
    })

# Aumentar cantidad
@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart:cart_view')

# Disminuir cantidad
@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart:cart_view')

# Eliminar ítem del carrito
@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart:cart_view')

# Vista de checkout (finalizar compra)
@login_required
def checkout_view(request):
    items = CartItem.objects.filter(user=request.user)
    if not items.exists():
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('cart:cart_view')

    total = sum(item.subtotal() for item in items)
    
    # Borra los items del carrito
    items.delete()

    # Muestra el mensaje de confirmación
    messages.success(request, f"Gracias por tu compra. Total pagado: ${total:.2f}")

    # Renderiza un template especial de confirmación
    return render(request, 'static_templates/cart/checkout_success.html', {
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Verifica si ya está en el carrito
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()

    messages.success(request, f'{product.name} fue añadido al carrito.')
    return redirect('cart:cart_view')