from django.shortcuts import render
from expensetracker.models import Transaction, Category, Savings
from django.db.models import Sum
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from expensetracker.get_transactions import get_transactions
from dashboard.filters import TransactionFilter


@login_required(login_url='login')
def dashboard(request):
    """
    View that returs the dashboard page.
    """

    income, expense, saving_goals = get_transactions(request)
    
    # Get categories from the transactions
    categories = Transaction.objects.filter(user=request.user).values('category__name').annotate(
        Sum('amount')
    )
    # Filter the categories
    transaction_filter = TransactionFilter(request.GET, queryset=categories, user=request.user)

    # Pagination
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "income": income,
        "expense": expense,
        "saving_goals": saving_goals,
        'categories': transaction_filter.qs,
        "page_obj": page_obj,
        'form': transaction_filter.form
    }
    return render(request, 'dashboard.html', context)
