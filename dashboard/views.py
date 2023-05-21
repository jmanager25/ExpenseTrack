from django.shortcuts import render
from expensetracker.models import Transaction, Category, Savings
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth

def dashboard(request):
    # Get total income
    income = Transaction.objects.filter(
        user=request.user, transaction_type='Income').aggregate(
            Sum('amount'))['amount__sum'] or 0
    # Get total expense
    expense = Transaction.objects.filter(
        user=request.user, transaction_type='Expense').aggregate(
            Sum('amount'))['amount__sum'] or 0
    # Get total savings
    saving_goals = Transaction.objects.filter(
        user=request.user, transaction_type='Saving Goal').aggregate(
            Sum('amount'))['amount__sum'] or 0
    
    # Get months and years from the transactions
    years = Transaction.objects.filter(user=request.user).annotate(
        year=ExtractYear('date')).values('year')

    months = Transaction.objects.filter(user=request.user).annotate(
        month=ExtractMonth('date')).values('month')

    # Get categories from the transactions
    categories = Transaction.objects.filter(user=request.user).values('category__name').annotate(
        Sum('amount')
    )
    context = {
        "income": income,
        "expense": expense,
        "saving_goals": saving_goals,
        'years': years,
        'months': months,
        'categories': categories
    }
    return render(request, 'dashboard.html', context)
