# Generated by Django 3.2.23 on 2024-06-25 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0004_alter_image_options'),
        ('catalog_app', '0018_auto_20240612_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='image_app.image', verbose_name='Изображение'),
        ),
    ]