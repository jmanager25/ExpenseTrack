from django.shortcuts import render
from django.views.generic.edit import CreateView
from expensetracker.models import Savings
from django.urls import reverse_lazy
from django.contrib import messages


def savings(request):
    return render(request, 'savings.html')


class SavingsCreateView(CreateView):
    """
    View that allows users to add saving goals.
    """
    model = Savings
    template_name = "add_savings.html"
    fields = ['name', 'description',
              'target_amount', 'target_date', 'progress']
    success_url = reverse_lazy('savings')

    def form_valid(self, form):
        """
        Ensures that the user who submitted the form is associated with the
        data, to keep track which user created the saving goals.
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Saving goal added successfully!')
        return super().form_valid(form)
