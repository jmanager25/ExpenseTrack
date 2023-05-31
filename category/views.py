from django.shortcuts import render, redirect
from expensetracker.models import Category
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator


@login_required(login_url='login')
def category(request):
    """
    View that returs the categories page.
    """

    categories = Category.objects.filter(
        user=request.user)

    paginator = Paginator(categories, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        "page_obj": page_obj,
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

    def dispatch(self, request, *args, **kwargs):
        """
        Checks if the user is the owner of the category.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            messages.error(request, """Sorry, You dont have permission to
            access this category.""")
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        """
        Checks if the user is the owner of the category.
        """
        obj = self.get_object()
        if obj.user != self.request.user:
            messages.error(request, """Sorry, You dont have permission
            to access this category.""")
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CategoryDeleteView,
                     self).delete(request, *args, **kwargs)
