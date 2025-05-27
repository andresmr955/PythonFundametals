from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Name')
    description = forms.CharField(max_length=300, label='Description')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price')
    available = forms.BooleanField(initial=True, label='Available', required=False)
    photo = forms.ImageField(label='Photo', required=False)
    
    def save(self):
        data = self.cleaned_data
        Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available=data['available'],
            photo=data['photo']
        )