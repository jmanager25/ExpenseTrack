from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    INCOME = 'Income'
    EXPENSE = 'Expense'
    SAVING_GOAL = 'Saving Goal'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
        (SAVING_GOAL, 'Saving Goal')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateField(default=now)
    transaction_type = models.CharField(
        max_length=20, choices=TRANSACTION_TYPE_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.transaction_type


class Savings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField(default=now)

    objects = models.Manager()

    def __str__(self):
        return self.name
