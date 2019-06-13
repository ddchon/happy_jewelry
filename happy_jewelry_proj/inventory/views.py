from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def inventory(request):
    return render(request, 'inventory/inventory.html')

def list_items(request):
    items = Product.objects.all()

    context = {
        "description": items.description,
        "type": items.type,
        "price": items.price
    }

    return render(request, 'inventory/inventory.html', context)

