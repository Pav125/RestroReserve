# Generated by Django 5.0.6 on 2024-06-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('table_number', models.CharField(max_length=30)),
                ('lunch_or_dinner', models.CharField(choices=[('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('reserved', models.BooleanField(default=False)),
            ],
        ),
    ]
