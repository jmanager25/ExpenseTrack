from . import views
from django.urls import path

urlpatterns = [
    path('', views.savings, name='savings'),
    path('add/', views.SavingsCreateView.as_view(), name='add_savings'),
]
