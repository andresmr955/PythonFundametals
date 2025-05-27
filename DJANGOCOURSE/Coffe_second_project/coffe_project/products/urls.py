from django.urls import path
from .views import product_detail, ProductFormView

urlpatterns = [
    path('', product_detail, name='product_detail'),
    path('add/', ProductFormView.as_view(), name='add_product'),
]
