# Generated by Django 3.2.18 on 2023-05-07 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='Transaction_type',
            new_name='transaction_type',
        ),
    ]
