# Generated by Django 4.2.2 on 2023-07-14 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_subcategory_category'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_userregister',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place'),
        ),
    ]