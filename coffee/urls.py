from django.urls import path
from . import views  # Importing views from the same folder

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('menu/', views.menu, name='menu'),  # Menu page
    path('menu/coffee/', views.coffee_menu, name='coffee'),  # Coffee menu page
    path('menu/pastries/', views.pastry_menu, name='pastries'),  # Pastries menu page
    path('search/', views.search, name='search'),  # Search page
]
