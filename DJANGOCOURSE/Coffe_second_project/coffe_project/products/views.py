from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import Product  
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response


# Create your views here.
# def home(request):
#     return render(request, 'base.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def menu(request):
    product = Product.objects.first()
    return render(request, 'menu.html', {'product': product})

def main(request):
    
    return render(request, 'main.html')

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductFormView(FormView):
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)