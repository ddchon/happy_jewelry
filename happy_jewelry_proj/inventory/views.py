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

def cart(request):
    return render(request, 'happyjewelry_pages/cart.html')

def add_cart(request):
    if request.method == "POST":
        new_cart = Product(product_img=request.POST['image'],
                           description=request.POST['description'],
                           item_type=request.POST['item_type'],
                           price=request.POST['price'])
        new_cart.save()
    
    return render(request, 'happyjewelry_pages/cart.html')

