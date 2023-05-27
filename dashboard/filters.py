import django_filters
from expensetracker.models import Transaction

class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = Transaction
        fields = ['category']