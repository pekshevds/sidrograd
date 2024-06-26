# Generated by Django 3.2.23 on 2024-06-12 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0017_auto_20240131_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Наименование полное'),
        ),
        migrations.AlterField(
            model_name='good',
            name='pasteurization',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog_app.pasteurization', verbose_name='Пастеризация'),
        ),
    ]
