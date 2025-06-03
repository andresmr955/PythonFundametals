from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import RegisForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = RegisForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('products/product_detail')
#     else:
#         form = RegisForm()
#     return render(request, '', {'form': form})


class RegisterView(CreateView):
    form_class = RegisForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()

        login(self.request, user)
        return super().form_valid(form)
