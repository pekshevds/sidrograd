# Generated by Django 3.2.23 on 2024-01-11 05:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0010_auto_20240103_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Наименование')),
                ('value', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Крепость, %',
                'verbose_name_plural': 'Виды крепостей',
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Наименование')),
                ('value', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Объем, л',
                'verbose_name_plural': 'Виды объемов',
            },
        ),
        migrations.AlterField(
            model_name='good',
            name='strength',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog_app.strength', verbose_name='Крепость, %'),
        ),
        migrations.AlterField(
            model_name='good',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog_app.volume', verbose_name='Объем, л'),
        ),
    ]
