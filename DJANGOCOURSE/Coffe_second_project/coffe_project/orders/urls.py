from django.urls import path
from .views import  CreateOrderView  , order_detail
app_name = 'orders'

urlpatterns = [
    path('create_order/<int:product_id>/', CreateOrderView.as_view(), name='create_order'),
    path('order_detail/<int:product_id>/', order_detail, name='order_detail'),
]
