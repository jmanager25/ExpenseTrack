from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    SAVING_GOAL = 'saving_goal'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
        (SAVING_GOAL, 'Saving Goal')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateField()
    transaction_type = models.CharField(
        max_length=20, choices=TRANSACTION_TYPE_CHOICES)

    def __str__(self):
        return self.transaction_type


class Savings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()
    progress = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
