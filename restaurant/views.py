from django.shortcuts import render
from .models import Category, Item
# Create your views here.

def restaurant(request):
    items=Item.objects.all()
    context = {'items':items}
       
    return render(request, 'restaurant.html', context)

def accomodation(request):
    items=Item.objects.all()
    context = {'items':items}
       
    return render(request, 'accomodation.html', context)