from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


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
