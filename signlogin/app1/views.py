from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .import forms
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Pass didn't match")
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        # Check if both username and password are provided
        if username and password:
            # Attempt to authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                return redirect('home')  # Redirect to home page
            else:
                # Authentication failed, show error message
                return HttpResponse("Username or Password is incorrect")

        else:
            # Username or password is missing
            return HttpResponse("Please provide both username and password")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def main(request):
    return render(request,'main.html')

@login_required(login_url='login')
def bin_info(request):
    app1=Bin.objects.all()
    return render(request,'bininfo.html',{
        "app1":app1,
    })

@login_required(login_url='login')
def add_bin(request):
    if request.method =="POST":
        form = forms.Binform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("add bin done")

    else:
        form = forms.Binform()
    return render(request,'forms.html',{
        "form":form,
    })

@login_required(login_url='login')
def delete_bin(request,p_id):
    Bin.objects.get(pk=p_id).delete()
    return redirect('home')
