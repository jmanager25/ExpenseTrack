from . import views
from django.urls import path

urlpatterns = [
    path('', views.category, name='category'),
    path('add/', views.CategoryCreateView.as_view(),
         name='add_category'),
    path('edit/<int:pk>/', views.CategoryUpdateView.as_view(),
         name='edit_category'),
]
