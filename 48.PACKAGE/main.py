from ecommerce.inventory.inventory import add_product, remove_product
from ecommerce.sales.sales import process_sales

add_product("iphone", 10)
remove_product("Laptop")
process_sales("iphone", 1)