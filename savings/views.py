from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from expensetracker.models import Savings, Transaction
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url='login')
def savings(request):
    """
    View that returs the saving page and allows user to see the
    saving goals.
    """
    saving_goals = Savings.objects.filter(
        user=request.user).order_by('target_date')

    for saving_goal in saving_goals:
        saved_money = Transaction.objects.filter(
          user=request.user,
          saving_goal=saving_goal,
          transaction_type='Saving Goal').aggregate(
            Sum('amount'))['amount__sum'] or 0

        progress = (saved_money / saving_goal.target_amount) * 100
        saving_goal.progress = progress
        saving_goal.save()

    context = {
        'saving_goals': saving_goals
    }
    return render(request, 'savings.html', context)


class SavingsCreateView(LoginRequiredMixin, CreateView):
    """
    View that allows users to add saving goals.
    """
    model = Savings
    template_name = "add_savings.html"
    fields = ['name', 'description',
              'target_amount', 'target_date']
    success_url = reverse_lazy('savings')
    login_url = 'login'

    def form_valid(self, form):
        """
        Ensures that the user who submitted the form is associated with the
        data, to keep track which user created the saving goals.
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Saving goal added successfully!')
        return super().form_valid(form)


class SavingsUpdateView(LoginRequiredMixin, UpdateView):
    """
    View that allows users to update existing Savings.
    """
    model = Savings
    template_name = "edit_savings.html"
    fields = ['name', 'description',
              'target_amount', 'target_date']
    success_url = reverse_lazy('savings')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Checks if the user is the owner of the saving goal.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            messages.error(request, """Sorry, You dont have permission to
            access this Saving goal.""")
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Ensures that the user who submit the form is associated with the
        data, to keep track which user updated the saving goals.
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Sanving goal updated successfully!')
        return super().form_valid(form)


class SavingsDeleteView(LoginRequiredMixin, DeleteView):
    """
    View that allows users to Delete existing Saving goals.
    """
    model = Savings
    template_name = "delete_savings.html"
    success_url = reverse_lazy('savings')
    success_message = "Saving goal deleted susccesfully"
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Checks if the user is the owner of the saving goal.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            messages.error(request, """Sorry, You dont have permission to
            access this Saving goal.""")
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SavingsDeleteView,
                     self).delete(request, *args, **kwargs)
