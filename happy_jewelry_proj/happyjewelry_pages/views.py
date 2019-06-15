from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from django.contrib import messages


def index(request):
    return render(request, 'happyjewelry_pages/home.html')

def contact(request):
    return render(request, 'happyjewelry_pages/contact.html')

def send_msg(request):
    if request.method == "POST":
        new_msg = Message(name=request.POST['name'],
                           phone=request.POST['phone'],
                           email=request.POST['email'],
                           message=request.POST['message'])
        new_msg.save()

        return render(request, 'happyjewelry_pages/sent.html')   