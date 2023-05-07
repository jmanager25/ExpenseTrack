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

    def get_context_data(self, **kwargs):
        """
        Allows the transaction choises to be dinamically 
        rendered in the template
        """
        context = super().get_context_data(**kwargs)
        context['transaction_type_choices'
                ] = Transaction.TRANSACTION_TYPE_CHOICES
        return context
