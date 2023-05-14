from . import views
from django.urls import path

urlpatterns = [
    path('', views.landin_page, name='landing-page'),
    path('home/', views.home, name='home'),
    path('add/', views.TransactionCreateView.as_view(),
         name='add_transaction'),
    path('edit/<int:pk>/', views.TransactionUpdateView.as_view(),
         name='edit_transaction')
]
