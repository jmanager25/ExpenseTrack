from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Transaction, Category, Savings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum
from expensetracker.get_transactions import get_transactions


def landin_page(request):
    """
    View that returs the landing page. the first page that the
    users see when they enter the website.
    """
    return render(request, "index.html")


@login_required(login_url='login')
def home(request):
    """
    View that returs the home page and allows user to see the
    transaction list.
    """
    transactions = Transaction.objects.filter(
        user=request.user).order_by('-date')

    income, expense, saving_goals = get_transactions(request)
    balance = income - expense - saving_goals

    paginator = Paginator(transactions, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "transactions": transactions,
        "page_obj": page_obj,
        "income": income,
        "expense": expense,
        "saving_goals": saving_goals,
        "balance": balance
    }

    return render(request, "home.html", context)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """
    View that allows users to add transactions.
    """
    model = Transaction
    template_name = "add_transaction.html"
    fields = ['transaction_type', 'date', 'category', 'amount',
              'description', 'saving_goal']
    success_url = reverse_lazy('home')
    login_url = 'login'

    def get_form(self, *args, **kwargs):
        """
        Customizes the form to display only the categories and saving goals
        created by the current user.
        """
        form = super().get_form(*args, **kwargs)
        form.fields['category'].queryset = Category.objects.filter(
            user=self.request.user)
        form.fields['saving_goal'].queryset = Savings.objects.filter(
            user=self.request.user)
        return form

    def form_valid(self, form):
        """
        Ensures that the user who submitted the form is associated with the
        data, to keep track which user added the transaction
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Transaction added successfully!')
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    """
    View that allows users to update existing transactions.
    """
    model = Transaction
    template_name = "edit_transaction.html"
    fields = [
        'transaction_type',
        'date',
        'category',
        'amount',
        'description',
        'saving_goal'
    ]
    success_url = reverse_lazy('home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Checks if the user is the owner of the transaction.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            messages.error(request, """Sorry, You dont have permission
            to access this transaction.""")
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def get_form(self, *args, **kwargs):
        """
        Customizes the form to display only the categories and saving goals
        created by the current user.
        """
        form = super().get_form(*args, **kwargs)
        form.fields['category'].queryset = Category.objects.filter(
            user=self.request.user)
        form.fields['saving_goal'].queryset = Savings.objects.filter(
            user=self.request.user)
        return form

    def form_valid(self, form):
        """
        Ensures that the user who submit the form is associated with the
        data, to keep track which user updated the transaction
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Transaction updated successfully!')
        return super().form_valid(form)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    """
    View that allows users to Delete existing transactions.
    """
    model = Transaction
    template_name = "delete_transaction.html"
    context_object_name = 'transaction'
    success_url = reverse_lazy('home')
    login_url = 'login'
    success_message = "Transaction deleted susccesfully"

    def dispatch(self, request, *args, **kwargs):
        """
        Checks if the user is the owner of the transaction.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            messages.error(request, """Sorry, You dont have permission to
            access this transaction.""")
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TransactionDeleteView,
                     self).delete(request, *args, **kwargs)
