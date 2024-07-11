# Generated by Django 3.2.23 on 2024-07-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0004_rename_address_point'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='point',
            options={'verbose_name': 'Адрес доставки ', 'verbose_name_plural': 'Адреса доставки'},
        ),
        migrations.AddField(
            model_name='point',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Адрес'),
        ),
    ]
