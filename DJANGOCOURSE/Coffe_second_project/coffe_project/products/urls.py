from django.urls import path
from .views import ProductFormView, ProductListView, main, product_detail

# app_name = 'products'

urlpatterns = [
    path('main/', main, name='product_detail'),
    path('menu/', product_detail, name='product_menu'),
    path('add/', ProductFormView.as_view(), name='add_product'),
    path('product_list/', ProductListView.as_view() , name='product_list')
]
