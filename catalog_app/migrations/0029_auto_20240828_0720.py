# Generated by Django 3.2.23 on 2024-08-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0028_merge_20240820_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='country',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='filtering',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='gassing',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='good',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='pasteurization',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='strength',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='style',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='trademark',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='typeoffermentation',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='marked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Пометка'),
        ),
    ]