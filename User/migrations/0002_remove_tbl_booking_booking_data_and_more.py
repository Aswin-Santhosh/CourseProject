# Generated by Django 4.2.2 on 2023-08-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_booking',
            name='booking_data',
        ),
        migrations.AddField(
            model_name='tbl_booking',
            name='booking_date',
            field=models.DateField(auto_now=True),
        ),
    ]
