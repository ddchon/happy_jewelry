from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def inventory(request):
    return render(request, 'inventory/inventory.html')

def list_items(request):

    context = {
            "items": Product.objects.all(),
        }

    return render(request, 'inventory/inventory.html', context)

