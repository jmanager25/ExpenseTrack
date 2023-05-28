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
    View that allow users to create category.
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


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    View that allow users to update existing categories.
    """
    model = Category
    template_name = "edit_category.html"
    fields = ['name']
    success_url = reverse_lazy('category')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Category updated successfully!')
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """
    View that allows users to Delete existing categories.
    """
    model = Category
    template_name = "delete_category.html"
    success_url = reverse_lazy('category')
    login_url = 'login'
    success_message = "Category deleted susccesfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CategoryDeleteView,
                     self).delete(request, *args, **kwargs)