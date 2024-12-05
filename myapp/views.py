from django.shortcuts import render
from .models import Items

# Create your views here.

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def store(request):
    items = Items.objects.all()
    context = {
        'items':items
    }
    return render(request, 'store.html', context)


def details(request, pk):
    item = Items.objects.get(id = pk)
    context = {
        'item':item
    }
    return render(request, 'details.html', context)


