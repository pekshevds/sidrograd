# Generated by Django 3.2.23 on 2024-06-27 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0024_auto_20240627_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='good',
            name='filtering',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.filtering', verbose_name='Фильтрация'),
        ),
        migrations.AlterField(
            model_name='good',
            name='gassing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.gassing', verbose_name='Газация'),
        ),
        migrations.AlterField(
            model_name='good',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.manufacturer', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='good',
            name='pasteurization',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.pasteurization', verbose_name='Пастеризация'),
        ),
        migrations.AlterField(
            model_name='good',
            name='strength',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.strength', verbose_name='Крепость, %'),
        ),
        migrations.AlterField(
            model_name='good',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.style', verbose_name='Стиль'),
        ),
        migrations.AlterField(
            model_name='good',
            name='trade_mark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.trademark', verbose_name='Торговая марка'),
        ),
        migrations.AlterField(
            model_name='good',
            name='type_of_fermentation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.typeoffermentation', verbose_name='Тип ферментации'),
        ),
        migrations.AlterField(
            model_name='good',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.unit', verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='good',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.volume', verbose_name='Объем, л'),
        ),
    ]
