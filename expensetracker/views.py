from django.shortcuts import render
from django.views.generic import CreateView
from .models import Transaction, Category


def home(request):
    """
    View that returs the home page
    """
    return render(request, "index.html")


class TransactionCreateView(CreateView):
    """
    View that allows to add transactions
    """
    model = Transaction
    template_name = "add_transaction.html"
    fields = ['transaction_type', 'date', 'category', 'amount', 'description']
