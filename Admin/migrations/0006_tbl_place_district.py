# Generated by Django 4.2.2 on 2023-07-11 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_place',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district'),
        ),
    ]
