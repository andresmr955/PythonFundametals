import requests

def get_products(product_name: str) -> str:
    url = "https://api.escuelajs.co/api/v1/products"
    response = requests.get(url)
    response.raise_for_status()
    products = response.json()

    # Buscar por nombre
    for product in products:
        if product_name.lower() in product["title"].lower():
            return f"Found: {product['title']} - Price: ${product['price']}"

    return "Product not found."

print(get_products("Classic Grey Hooded Sweatshirt"))
