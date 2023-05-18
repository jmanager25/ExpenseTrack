from django.shortcuts import render


def savings(request):
    return render(request, 'savings.html')
