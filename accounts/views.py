import re
from django.shortcuts import render, redirect

# Create your views here.
def signn(request):
    return render(request,'accounts/signin.html')
def signp(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            new=User.object.create(email='go@gmail.com',firstname=firstname,lastname=lastname,address=address)
            new.set_password(password1)
            new.save()
            print(new)
    return render(request,'accounts/signup.html')