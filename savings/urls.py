from . import views
from django.urls import path

urlpatterns = [
    path('', views.savings, name='savings'),
]
