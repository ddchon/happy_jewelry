from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

def index(request):
    return render(request, 'happyjewelry_pages/home.html')

def contact(request):
    return render(request, 'happyjewelry_pages/contact.html')


def createmessage(request):
    if request.method == 'POST':
        new_message = Message(name=request.POST['name'],
                            phone=request.POST['phone'],
                            email=request.POST['email'],
                            message=request.POST['message'])
        new_message=Message()
                        # user_contact.name=request.POST.get('name')
                        # user_contact.name=request.POST.get('phone')
                        # user_contact.name=request.POST.get('email')
                        # user_contact.name=request.POST.get('message')

        new_message.save()

        return render(request, 'admin/')
    else:
        return render(request, 'admin/')