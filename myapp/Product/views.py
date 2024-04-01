from django.shortcuts import render
from .models import Dish

def products(request):
    dishes = Dish.objects.all()
    return render(request, 'Product.html', {'dishes': dishes})
