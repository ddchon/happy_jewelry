
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact_us"),
    path("send/", views.send_msg, name="submit_msg"),
]