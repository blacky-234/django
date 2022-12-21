from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . models import User

# testung
from django.views.generic import TemplateView

# Create your views here.


def login(request):
    return render(request, 'auth/_login.html')


def signup(request):
    if(request.method == "GET"):
        return render(request, 'auth/_signup.html');
    if request.method == "POST":
        name = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=name, email=email, password=password, phone=phone)
        user.save()
        return redirect('login')
    else:
        return redirect('signup')

        


# def newsignup(request):
#     if request.method == "POST":
#         name = request.POST['username']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         password = request.POST['password']
#         user = User.objects.create_user(username=name, email=email, password=password, phone=phone)
#         user.save()
#         return login(request)
#     else:
#         return redirect('signup')


def alogin(request):
    if request.method == "POST":
        lname = request.POST['email_address']
        passwd = request.POST["password"]
        user = authenticate(username=lname, password=passwd)
        if user.is_authenticated:               
            return render(request, 'album/album.html') 
        else:
            # TODO: check login header connections
            return login(request)
# @logout
# def logout_view(request):
#     logout(request)
#     return HttpResponse("<h1> logout successfully </h1>")
    