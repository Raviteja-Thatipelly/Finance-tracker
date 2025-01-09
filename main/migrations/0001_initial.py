# Generated by Django 5.1.4 on 2025-01-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_to', models.CharField(blank=True, max_length=100, null=True)),
                ('mode_of_payment', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('time_stamp_created', models.DateTimeField(auto_now_add=True)),
                ('time_stamp_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
