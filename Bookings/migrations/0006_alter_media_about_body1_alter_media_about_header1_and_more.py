# Generated by Django 5.0.6 on 2024-06-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0005_media_delete_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='about_body1',
            field=models.ImageField(blank=True, null=True, upload_to='about_body1/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='about_header1',
            field=models.ImageField(blank=True, null=True, upload_to='about_header1/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='about_header2',
            field=models.ImageField(blank=True, null=True, upload_to='about_header2/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='about_header3',
            field=models.ImageField(blank=True, null=True, upload_to='about_header3/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='register_image',
            field=models.ImageField(blank=True, null=True, upload_to='register_image/'),
        ),
    ]
