# Generated by Django 3.2.23 on 2024-10-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0031_good_show_price_by_liter'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='price_by_liter',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='Цена за литр'),
        ),
    ]
