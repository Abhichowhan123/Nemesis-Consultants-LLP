from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
from .models import customer
def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method =="POST":
        NAME = request.POST.get("name")
        USERNAME = request.POST.get("username")
        EMAIL = request.POST.get("email")
        PHONE = request.POST.get("phone")
        PASSWORD = request.POST.get("password")
        CONFIRM_PASSWORD = request.POST.get("confirm_password")
        if PASSWORD == CONFIRM_PASSWORD:
            x  = customer(Name=NAME,Username=USERNAME,Email=EMAIL,Phone=PHONE,Password=PASSWORD )
            x.save()
            return render(request, "login.html")
        else:
            return render(request,"signup.html")
    else:
        return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        EMAIL = request.POST.get("email")
        PASSWORD = request.POST.get("password")
        user = authenticate(Email=EMAIL,Password=PASSWORD )
        if user is None:
            auth.login(request ,user)
            return render(request,"signup.html")
        else:
            return render(request, "")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")