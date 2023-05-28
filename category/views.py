from django.shortcuts import render
from expensetracker.models import Category
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


@login_required(login_url='login')
def category(request):
    """
    View that returs the categories page.
    """

    categories = Category.objects.filter(
        user=request.user)

    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
    View that allows users to create category.
    """
    model = Category
    template_name = "add_category.html"
    fields = ['name']
    success_url = reverse_lazy('category')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Category created successfully!')
        return super().form_valid(form)
