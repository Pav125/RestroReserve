# Generated by Django 5.0.6 on 2024-07-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0004_alter_feedbacks_email_alter_feedbacks_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='feedback',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
