from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product  # Importa el modelo Product

# Create your views here.
def home(request):
    return render(request, 'base.html')

def product_detail(request):
    product = Product.objects.first()  # O usa algún filtro si tienes más de un producto
    return render(request, 'base.html', {'product': product})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guardamos el nuevo producto en la base de datos
            return redirect('success')  # Redirige a una página de éxito o lo que prefieras
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})