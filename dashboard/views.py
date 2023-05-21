from django.shortcuts import render
from expensetracker.models import Transaction, Category, Savings
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from expensetracker.get_transactions import get_transactions


@login_required(login_url='login')
def dashboard(request):
    """
    View that returs the dashboard page.
    """
    income, expense, saving_goals = get_transactions(request)
    
    # Get months and years from the transactions
    years = Transaction.objects.filter(user=request.user).annotate(
        year=ExtractYear('date')).values('year')

    months = Transaction.objects.filter(user=request.user).annotate(
        month=ExtractMonth('date')).values('month')

    # Get categories from the transactions
    categories = Transaction.objects.filter(user=request.user).values('category__name').annotate(
        Sum('amount')
    )
    # Pagination
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "income": income,
        "expense": expense,
        "saving_goals": saving_goals,
        'years': years,
        'months': months,
        'categories': categories,
        "page_obj": page_obj,
    }
    return render(request, 'dashboard.html', context)
