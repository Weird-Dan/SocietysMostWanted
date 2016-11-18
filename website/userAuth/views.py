from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def UserView(request, pk):
    user = get_object_or_404(User, pk=pk)
    eu = user.extuser_set.get()
    return render(request, "userAuth/user.html", {"user":user, "eu":eu})

def Login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("smw:flow")
    else:
        return redirect("smw:index")

def Logout(request):
    logout(request)
    return redirect("smw:index")
