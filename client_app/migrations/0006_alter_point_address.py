# Generated by Django 3.2.23 on 2024-07-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0005_auto_20240711_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='address',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Адрес'),
        ),
    ]
