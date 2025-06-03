from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from products.models import Product
from .models import Order, OrderProduct

# Create your views here.

# def main(request):
#     return render(request, 'orders/orders.html')


class OrderView(TemplateView):
    template_name = "orders/orders.html"


# @login_required
# def create_order(request, product_id):
#     product = Product.objects.get(id=product_id)


#     order = Order.objects.filter(user=request.user, order_status='pending').first()

#     if not order:
#         order = Order.objects.create(user=request.user, order_status='pending')

#     order_product = OrderProduct.objects.filter(order=order, product=product).first()

#     if order_product:
#         order_product.quantity += 1
#         order_product.save()
#     else:

#         OrderProduct.objects.create(order=order, product=product, quantity=1)

#     return redirect('orders:order_detail', order_id=order.id)


class CreateOrderView(LoginRequiredMixin, View):
    def get_redirect_order(self, request, product_id):
        order = Order.objects.filter(user=request.user, order_status="pending").first()
        if not order:
            order = Order.objects.create(user=request.user, order_status="pending")

        return redirect("orders:order_detail", order_id=order.id)

    def post(self, request, product_id):
        order = Order.objects.filter(user=request.user, order_status="pending").first()
        if not order:
            order = Order.objects.create(user=request.user, order_status="pending")

        product = get_object_or_404(Product, id=product_id)
        order_product = OrderProduct.objects.filter(
            order=order, product=product
        ).first()

        if order_product:
            order_product.quantity += 1
            order_product.save()
        else:
            OrderProduct.objects.create(order=order, product=product, quantity=1)

        return self.get_redirect_order(request, product_id)

    def get(self, request, product_id):
        return self.get_redirect_order(request, product_id)


# @login_required
# def order_detail(request, product_id):
#     order = get_object_or_404(Order, id=product_id)

#     if order.user != request.user:
#         return redirect('orders:order_list')

#     total = 0
#     for order_product in order.order_products.all():
#         total += order_product.product.price * order_product.quantity

#     context = {
#         'order': order,
#         'total': total, # Pass the calculated total to the template
#     }
#     return render(request, 'orders/order_detail.html', context)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "order_id"

    def get_object(self, queryset=None):
        order = super().get_object(queryset)
        if order.user != self.request.user:
            return redirect("orders:order_list")
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = context["order"]
        total = sum(
            item.product.price * item.quantity for item in order.order_products.all()
        )

        context["total"] = total
        return context
