# Generated by Django 3.2.23 on 2023-12-13 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0008_auto_20231213_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog_app.unit', verbose_name='Единица измерения'),
        ),
    ]