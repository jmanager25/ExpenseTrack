from django.shortcuts import render
from expensetracker.models import Transaction, Category, Savings
from django.db.models import Sum

def dashboard(request):
    income = Transaction.objects.filter(
        user=request.user, transaction_type='Income').aggregate(
            Sum('amount'))['amount__sum'] or 0

    expense = Transaction.objects.filter(
        user=request.user, transaction_type='Expense').aggregate(
            Sum('amount'))['amount__sum'] or 0

    saving_goals = Transaction.objects.filter(
        user=request.user, transaction_type='Saving Goal').aggregate(
            Sum('amount'))['amount__sum'] or 0

    context = {
        "income": income,
        "expense": expense,
        "saving_goals": saving_goals
    }
    return render(request, 'dashboard.html', context)
