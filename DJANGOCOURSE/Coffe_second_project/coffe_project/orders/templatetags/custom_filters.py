from django import template

register = template.Library()


# Filtro para multiplicar el precio por la cantidad
@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return 0
