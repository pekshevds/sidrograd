# Generated by Django 3.2.23 on 2024-01-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0015_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(blank=True, db_index=True, default='', max_length=3, null=True, verbose_name='Код оп ОКСМ'),
        ),
    ]