from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_items, name="inventory"),
    path("cart/", views.cart, name="cart"),
    path("add", views.add_cart, name="add"),
]