# Generated by Django 3.2.23 on 2024-08-28 07:23

from django.db import migrations, models
import django.db.models.deletion
import order_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0016_auto_20240828_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default=order_app.models.default_order_status, null=True, on_delete=django.db.models.deletion.PROTECT, to='order_app.orderstatus', verbose_name='Статус'),
        ),
    ]
