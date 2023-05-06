from django.shortcuts import render


def home(request):
    """
    Views that returs the home page
    """
    return render(request, "index.html")
