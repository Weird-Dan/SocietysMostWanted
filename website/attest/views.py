from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def Detail(request, pk):
    usr = get_object_or_404(User, pk=pk)
    return render(request, "attest/detail.html", {"User":usr})

def Login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("smw:index")
    else:
        return redirect("attest:lgn")

def Logout(request):
    logout(request)
    return redirect("smw:index")

def lgn(request):
    return render(request, 'attest/login.html')

def Register(request):
    if request.POST:
        ps1 = request.POST['password1']
        ps2 = request.POST['password2']
        un = request.POST['username']
        em = request.POST['email']
        if ps1 == ps2:
            if un and em:
                if len(User.objects.filter(email=em))==0 and len(User.objects.filter(username=un))==0:
                    user = User.objects.create_user(un, em, ps1)
                    user.save()
                    usr = authenticate(username=un, password=ps1)
                    if user is not None:
                        login(request, user)
                        return redirect("smw:index")
                    else:
                        return redirect("attest:lgn")
                #else:
        #else:
    return redirect('attest:lgn')
