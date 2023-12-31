# Generated by Django 4.2.7 on 2023-12-05 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0007_alter_user_client_alter_user_password'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client_app', '0001_initial'),
        ('order_app', '0003_alter_order_options_alter_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client_app.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client_app.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order_app.contract', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order_app.customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='order',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order_app.organization', verbose_name='Организация'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
