from .models import Transaction
from django.db.models import Sum

def get_transactions(request):
    """
    gets the transaction tupes total amount.
    """
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

    return income, expense, saving_goals