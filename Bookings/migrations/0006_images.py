# Generated by Django 5.0.6 on 2024-06-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0005_delete_table_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]