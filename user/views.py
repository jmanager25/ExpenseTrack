from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    """
    Allows users to make the registrantion on the webpage
    """
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

    user = User.objects.filter(email=email).exists()

    if user:
        messages.error(request, '''You have already registered
                       please log in instead''')
        return render(request, 'register.html')

    user = User.objects.create_user(
        username=username, email=email, password=password)
    user.save()
    messages.success(request, 'Account successfully created')
    return render(request, 'register.html')


def log_in(request):
    """
    Alows registered users to login in the website
    """
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        messages.success(request, 'Login successfull')
        return render(request, 'home.html')
    else:
        messages.error(request, 'Incorrect username or password')
        return render(request, 'login.html')


def log_out(request):
    logout(request)
    messages.success(request, 'You have been succesfully logged out')
    return render(request, 'index.html')
