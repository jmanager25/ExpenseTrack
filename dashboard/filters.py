import django_filters
from expensetracker.models import Transaction, Category

class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = Transaction
        fields = ['category']

    def __init__(self, *args, **kwargs):
        """
        Initialize the TransactionFilter instance and filters the 
        categories to display only the categories
        created by the current user.
        """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.filters['category'].queryset =  Category.objects.filter(user=user)