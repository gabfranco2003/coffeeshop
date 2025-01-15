from django.shortcuts import render
from .models import Coffee, Pastry, Tea, HeroImage

# Home view (for the home page)
def home(request):
    hero_images = HeroImage.objects.all()  # Query all hero images
    coffee_item = Coffee.objects.first()
    tea_item = Tea.objects.first()  # Same for tea
    pastry_item = Pastry.objects.first()  # Same for pastries

    return render(request, 'home.html', {
        'hero_images': hero_images,
        'coffee_item': coffee_item,
        'tea_item': tea_item,
        'pastry_item': pastry_item,
    })

# About view (for the about page)
def about(request):
    return render(request, 'about.html')

# Menu view (for the main menu page)
def menu(request):
    coffees = Coffee.objects.all()
    pastries = Pastry.objects.all()
    teas = Tea.objects.all()  # Correctly query the tea items
    return render(request, 'menu.html', {
        'coffees': coffees,
        'pastries': pastries,
        'teas': teas,  # Pass teas to the template
    })

# Coffee menu view (only coffee items)
def coffee_menu(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffee/coffee_menu.html', {'coffees': coffees})

# Tea menu view (only tea items)
def tea_menu(request):  # Renamed from pastry_menu to tea_menu
    teas = Tea.objects.all()  # Query all tea items
    return render(request, 'teas/tea_menu.html', {'teas': teas})

# Pastry menu view (only pastry items)
def pastry_menu(request):
    pastries = Pastry.objects.all()
    return render(request, 'pastries/pastry_menu.html', {'pastries': pastries})

# Search view (for the search page)
def search(request):
    query = request.GET.get('query', '')  # Get search query from the search form

    if query:  # Only search if query is not empty
        coffee_results = Coffee.objects.filter(name__icontains=query)
        pastry_results = Pastry.objects.filter(name__icontains=query)
        tea_results = Tea.objects.filter(name__icontains=query)  # Correct query for tea items
    else:
        coffee_results = []
        pastry_results = []
        tea_results = []  # Initialize tea_results to prevent errors

    return render(request, 'search_results.html', {
        'query': query,
        'coffee_results': coffee_results,
        'pastry_results': pastry_results,
        'tea_results': tea_results,  # Pass tea_results to the template
    })
