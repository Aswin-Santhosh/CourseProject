# Generated by Django 4.2.2 on 2023-07-24 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_tbl_product_shop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_product',
            old_name='subcategory',
            new_name='category',
        ),
    ]
