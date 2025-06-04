from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3


def check_order_status(status: OrderStatus):
    if status == OrderStatus.PENDING:
        return "Order is still pending"
    elif status == OrderStatus.SHIPPED:
        return "Order is still shipped"
    elif status == OrderStatus.DELIVERED:
        return "Order  is delivered"
    
print(check_order_status(OrderStatus.PENDING))
print(check_order_status(OrderStatus.SHIPPED))
print(check_order_status(OrderStatus.DELIVERED))