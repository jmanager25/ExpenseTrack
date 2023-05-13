# Generated by Django 3.2.18 on 2023-05-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker', '0002_rename_transaction_type_transaction_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense'), ('Saving Goal', 'Saving Goal')], max_length=20),
        ),
    ]
