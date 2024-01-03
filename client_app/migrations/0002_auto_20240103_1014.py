# Generated by Django 3.2.23 on 2024-01-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
    ]
