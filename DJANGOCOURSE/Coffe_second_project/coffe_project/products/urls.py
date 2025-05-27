from django.urls import path
from .views import product_detail

urlpatterns = [
    path('', product_detail, name='product_detail'),
]
