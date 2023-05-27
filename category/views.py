from django.shortcuts import render
from expensetracker.models import Category
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def category(request):
    """
    View that returs the categories page.
    """
    return render(request, 'category.html')
