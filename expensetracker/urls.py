from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.TransactionCreateView.as_view(), name='add_transaction')
]
