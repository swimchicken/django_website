from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import shop_item
import logging

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        money = request.POST.get('money')

        print(product_name, money)
        cart_item = shop_item(name=product_name, money=money)
        cart_item.save()
        return JsonResponse({'status': 'success', 'message': 'Item added to cart.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def show_cart(request):
    total_item = list(shop_item.objects.all())
    template = loader.get_template("index.html")
    context = {
        'total_item': total_item
    }

    print(context)
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def index_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def shop(request):
    template = loader.get_template('shop.html')
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
            wrong_password = True
            return render(request, "signup.html", {'wrong_password': wrong_password})
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
            wrong_password = True
            return render(request, "login.html", {'wrong_password': wrong_password})
    return render(request, "login.html")
