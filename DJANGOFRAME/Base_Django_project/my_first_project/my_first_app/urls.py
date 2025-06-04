"""
URL configuration for my_first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [

    path('', views.my_view_base, name='home'), 

    path("listed/", views.my_view_cars, name="car_list"),
    path('listed/<slug:slug>/', views.my_view_cars, name="car_list_slug"),

    path("detailed/<int:id>", views.my_view_two, name="detailed"),
    path("brand/<str:id>", views.my_view_two, name="brand"),
    path('name_creator/', views.print_my_name, name="print_my_name"),
    
    path('authors/<slug:slug>/', views.author_detail, name="author_detail"),
    # path('authors/', views.view_authors, name="view_authors_list"),
    path('authors/', views.AuthorsListView.as_view(), name = "view_authors_list"),

]
