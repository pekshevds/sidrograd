# Generated by Django 3.2.23 on 2024-01-17 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_auto_20240103_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Файл изображения'),
        ),
    ]