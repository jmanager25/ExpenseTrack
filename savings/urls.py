from . import views
from django.urls import path

urlpatterns = [
    path('', views.savings, name='savings'),
    path('add/', views.SavingsCreateView.as_view(), name='add_savings'),
    path('edit/<int:pk>/', views.SavingsUpdateView.as_view(),
         name='edit_savings'),
    path('delete/<int:pk>/', views.SavingsDeleteView.as_view(),
         name='delete_savings')
]
