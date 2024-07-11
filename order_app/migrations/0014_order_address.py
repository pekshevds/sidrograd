# Generated by Django 3.2.23 on 2024-07-11 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0006_alter_point_address'),
        ('order_app', '0013_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client_app.point', verbose_name='Адрес доставки'),
        ),
    ]
