from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from products.models import Product
from .models import Order, OrderProduct

# Create your views here.

def main(request):
    return render(request, 'orders/orders.html')

@login_required
def create_order(request, product_id):
    product = Product.objects.get(id=product_id)
    print(f"Producto seleccionado: {product.name}")


    order = Order.objects.filter(user=request.user, order_status='pending').first()
    print(f"Orden creada o recuperada: {order.id}")

    if not order:
        order = Order.objects.create(user=request.user, order_status='pending')
    
    order_product = OrderProduct.objects.filter(order=order, product=product).first()

    if order_product:
        order_product.quantity += 1
        order_product.save()
    else:

        OrderProduct.objects.create(order=order, product=product, quantity=1)
    
    return redirect('orders:order_detail', order_id=order.id)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    # Asegúrate de que solo se puedan ver las órdenes del usuario logueado
    if order.user != request.user:
        return redirect('orders:order_list')
    
    total = 0
    for order_product in order.order_products.all():
        total += order_product.product.price * order_product.quantity

    context = {
        'order': order,
        'total': total, # Pass the calculated total to the template
    }
    return render(request, 'orders/order_detail.html', context)