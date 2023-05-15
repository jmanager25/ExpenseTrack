from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Transaction, Category
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator


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
    paginator = Paginator(transactions, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "transactions": transactions,
        "page_obj": page_obj
    }
    return render(request, "home.html", context)


class TransactionCreateView(CreateView):
    """
    View that allows users to add transactions.
    """
    model = Transaction
    template_name = "add_transaction.html"
    fields = ['transaction_type', 'date', 'category', 'amount', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Ensures that the user who submitted the form is associated with the
        data, to keep track which user added the transaction
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Transaction added successfully!')
        return super().form_valid(form)


class TransactionUpdateView(UpdateView):
    """
    View that allows users to update existing transactions.
    """
    model = Transaction
    template_name = "edit_transaction.html"
    fields = ['transaction_type', 'date', 'category', 'amount', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Ensures that the user who submit the form is associated with the
        data, to keep track which user updated the transaction
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Transaction updated successfully!')
        return super().form_valid(form)


class TransactionDeleteView(DeleteView):
    """
    View that allows users to Delete existing transactions.
    """
    model = Transaction
    template_name = "delete_transaction.html"
    context_object_name = 'transaction'
    success_url = reverse_lazy('home')
    success_message = "Transaction deleted susccesfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TransactionDeleteView,
                     self).delete(request, *args, **kwargs)
