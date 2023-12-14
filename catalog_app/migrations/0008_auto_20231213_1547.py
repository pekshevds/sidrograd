# Generated by Django 3.2.23 on 2023-12-13 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0007_alter_good_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog_app.manufacturer', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='good',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog_app.unit', verbose_name='Единица измерения'),
        ),
    ]