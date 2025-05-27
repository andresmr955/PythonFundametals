from django.urls import path
from .views import product_detail, ProductFormView, product_list

urlpatterns = [
    path('', product_detail, name='product_detail'),
    path('add/', ProductFormView.as_view(), name='add_product'),
    path('product_list/', product_list, name='product_list')
]
