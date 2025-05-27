from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product  # Importa el modelo Product
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


# Create your views here.
def home(request):
    return render(request, 'base.html')

def product_detail(request):
    product = Product.objects.first()  # O usa algún filtro si tienes más de un producto
    return render(request, 'base.html', {'product': product})


def product_list(request):
    products = Product.objects.all
    context = {
        "products": products
    }
    return render(request, 'product_list.html', context )

class ProductFormView(FormView):
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)