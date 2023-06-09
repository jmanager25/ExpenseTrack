# Generated by Django 3.2.18 on 2023-05-13 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker', '0003_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='target_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
