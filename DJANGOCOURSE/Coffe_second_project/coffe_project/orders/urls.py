from django.urls import path
from .views import main, order_detail, create_order

app_name = 'orders'

urlpatterns = [
    path('create_order/<int:product_id>', create_order, name='create_order'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
]
