from django.shortcuts import render
from django.http import HttpResponse
from . import views

def index(request):
    return render(request, 'happyjewelry_pages/home.html')
    
def contact(request):
    return render(request, 'happyjewelry_pages/contact.html')