from django.shortcuts import render, redirect
from django.contrib.auth import login
# Create your views here.
from .forms import RegisForm

def register(request):
    if request.method == 'POST':
        form = RegisForm(request.POST)
        if form.is_valid():
            user = form.save()
            login((request, user))
            return redirect('products/product_detail')
    else:
        form = RegisForm()
    return render(request, 'registration/register.html', {'form': form})