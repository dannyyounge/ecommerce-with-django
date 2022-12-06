from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/',homep,name='homepage'),
    path('product/',prod, name='productpage'),
    path('checkout/',check,name='checkoutpage'),
    path('goto/',homepp,name='secondhome'),
]