from django.shortcuts import render

from ecomm.models import Category
from .models import *
# Create your views here.
def homep(request):
    catt=Category.objects.all()
    item=Item.objects.all()
    lake={'catt':catt,'item':item}
    return render(request, 'ecomm/home-page.html',lake)
def prod(request):
    return render(request, 'ecomm/product-page.html')
def check(request):
    return render(request, 'ecomm/checkout-page.html')
def homepp(request):
    return render(request,'ecomm/home-page.html')