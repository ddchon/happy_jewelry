from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Product

# Create your views here.
def inventory(request):
    return render(request, 'inventory/inventory.html')

def list_items(request):

    items = Product.objects.all()

    context = {
        "store_items": items
        }

    return render(request, 'inventory/inventory.html', context=context)

def cart(request):

    context = {
        "added_items": Product.objects.filter(add_to_cart=True)
    }
    
    return render(request, 'inventory/cart.html', context=context)

def grabbed(request):
    if request.method == "POST":

        to_add = Product.objects.get(id=request.POST['id'])

        to_add.add_to_cart = request.POST['grabbed']
        
        to_add.save()

        return redirect('inventory')
    
    return redirect('cart')

