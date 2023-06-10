from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


@login_required(login_url='login')
def index_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def LogoutPage(request):
    logout(request)
    return redirect('login')


def SigupPage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        ename = request.POST.get('email')
        p1 = request.POST.get('password')
        p2 = request.POST.get('re_password')
        if p1 != p2:
            return HttpResponse("Your not ture")
        else:
            my_user = User.objects.create_user(uname, ename, p1)
            my_user.save()
            return redirect('login')

    return render(request, "signup.html")


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request, "login.html")
