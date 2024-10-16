# Generated by Django 3.2.23 on 2024-10-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog_app", "0029_auto_20240828_0720"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="good",
            options={
                "ordering": ["trade_mark", "name"],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.AlterField(
            model_name="good",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=15,
                null=True,
                verbose_name="Цена за единицу",
            ),
        ),
    ]
