from django.urls import path
from .views import  CreateOrderView  , OrderDetailView
app_name = 'orders'

urlpatterns = [
    path('create_order/<int:product_id>/', CreateOrderView.as_view(), name='create_order'),
    path('order_detail/<int:product_id>/', OrderDetailView.as_view(), name='order_detail'),
]
