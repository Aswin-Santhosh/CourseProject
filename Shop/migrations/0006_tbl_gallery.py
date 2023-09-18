# Generated by Django 4.2.2 on 2023-07-24 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_alter_tbl_product_product_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='ProductDocs/ProductGallery/')),
                ('Cation', models.FileField(upload_to='')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product')),
            ],
        ),
    ]
