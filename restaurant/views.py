from django.shortcuts import render
from .models import Category, Item
from .forms import ReserveForm
# Create your views here.

def restaurant(request):
    items=Item.objects.all()
    drinks=Item.objects.filter(group__name='Drinks')
    meals=Item.objects.filter(group__name='Meals')
    context = {'drinks':drinks, 'meals':meals}
       
    return render(request, 'restaurant.html', context)

def accomodation(request):
    items=Item.objects.all()
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ReserveForm()
    context = {'items':items, 'form':form}

       
    return render(request, 'accomodation.html', context)

def contact(request):
    return render(request, 'contact.html', context)