# Generated by Django 4.2.2 on 2023-07-26 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0007_rename_cation_tbl_gallery_cation'),
        ('Guest', '0005_alter_tbl_shopregistration_shop_proof'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_data', models.IntegerField(auto_created=True)),
                ('booking_status', models.IntegerField(default=0)),
                ('booking_quantity', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userregister')),
            ],
        ),
    ]
