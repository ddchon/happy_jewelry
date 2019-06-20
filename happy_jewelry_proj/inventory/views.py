from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import Product

# Create your views here.
def inventory(request):
    return render(request, 'inventory/inventory.html')

def list_items(request):

    items = []

    if request.method == "POST":
        items = Product.objects.filter(item_type=request.POST['search'])

    else:
        items = Product.objects.all()
    
    context = {
        "stored_items": items
    }

    return render(request, "inventory/inventory.html", context=context)

def cart(request):

    add_item = Product.objects.filter(add_to_cart=True)

    total = 0
    for i in add_item:
        total += i.price

    context = {
        "added_items": add_item,
        "totals": total
    }
    
    return render(request, 'inventory/cart.html', context=context)

def grabbed(request):
    if request.method == "POST":

        to_add = Product.objects.get(id=request.POST['id'])

        to_add.add_to_cart = request.POST['grabbed']
        
        to_add.save()

        return redirect('cart')
    
    return redirect('inventory')




