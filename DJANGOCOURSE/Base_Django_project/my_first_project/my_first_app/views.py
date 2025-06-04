from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from my_first_app.models import Car, Author
from django.views.generic import TemplateView


# Create your views here.
def my_view_cars(request, slug=None):
    if slug:
        # Filtrar por slug, si no hay resultados, mostramos un mensaje adecuado
        car_list = Car.objects.filter(slug=slug)
        if not car_list:
                # Si no se encuentra ningún coche con ese slug
                car_list = []
                message = "No cars found with the provided slug."
        else:
                message = None
    else:
        # Si no se pasa el slug, mostramos todos los coches
        car_list = Car.objects.all()
        message = None

    context = {
        "car_list": car_list,
        "message": message,  # Mensaje de error si no se encuentra el slug
    }
        
        
    return render(request, "my_first_app/car_list.html", context)

def my_view_base(request):
      
     context = {
          "welcome_message": "Welcome to my site!",
     }
     return render(request, 'my_first_app/home.html', context)

def my_view_two(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def print_my_name(request):
    name = "Andres Marquez"
    return render(request, 'my_first_app/index.html', {'name': name})

# def view_authors(request):
#     authors_list = Author.objects.all()
#     message = None

#     if not authors_list:
              
#               message = "No authors found"
#     context = {
#         "authors_list": authors_list,
#         "message": message,
#     }

#     return render(request, 'my_first_app/authors.html', context)

class AuthorsListView(TemplateView):
     template_name = 'my_first_app/authors.html'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          authors_list = Author.objects.all()

          context["authors_list"] = authors_list
          if not authors_list.exists():
               context["message"] = "No authors found"
          return context
     
def author_detail(request, slug):
    author = get_object_or_404(Author, slug_author=slug)
    return render(request, 'my_first_app/profile.html', {"author": author})