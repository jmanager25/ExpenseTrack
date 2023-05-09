from django.shortcuts import render
from django.contrib.auth.models import User


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

    user = User.objects.create_user(
        username=username, email=email, password=password)
    user.save()
