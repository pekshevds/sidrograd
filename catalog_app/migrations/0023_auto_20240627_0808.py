# Generated by Django 3.2.23 on 2024-06-27 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0022_auto_20240625_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filtering',
            options={'ordering': ['name'], 'verbose_name': 'Фильрация', 'verbose_name_plural': 'Виды фильтрации'},
        ),
        migrations.AlterModelOptions(
            name='gassing',
            options={'ordering': ['name'], 'verbose_name': 'Газация', 'verbose_name_plural': 'Виды газации'},
        ),
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name'], 'verbose_name': 'Производитель', 'verbose_name_plural': 'Производители'},
        ),
        migrations.AlterModelOptions(
            name='pasteurization',
            options={'ordering': ['name'], 'verbose_name': 'Пастеризация', 'verbose_name_plural': 'Виды пастеризации'},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['name'], 'verbose_name': 'Спиль', 'verbose_name_plural': 'Стили'},
        ),
        migrations.AlterModelOptions(
            name='trademark',
            options={'ordering': ['name'], 'verbose_name': 'Торговая марка', 'verbose_name_plural': 'Торговые марки'},
        ),
        migrations.AlterModelOptions(
            name='typeoffermentation',
            options={'ordering': ['name'], 'verbose_name': 'Тип ферментации', 'verbose_name_plural': 'Типы ферментации'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['name'], 'verbose_name': 'Единица измерения', 'verbose_name_plural': 'Единицы измерения'},
        ),
        migrations.RemoveField(
            model_name='good',
            name='qnt',
        ),
    ]