# Generated by Django 3.2.23 on 2024-06-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0019_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='qnt',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='Остаток'),
        ),
    ]