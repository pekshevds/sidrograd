# Generated by Django 3.2.23 on 2024-08-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0006_alter_point_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='marked',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Пометка'),
        ),
        migrations.AddField(
            model_name='point',
            name='marked',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Пометка'),
        ),
    ]
