from . import views
from django.urls import path

urlpatterns = [
    path('', views.category, name='category'),
]
