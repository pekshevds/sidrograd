# Generated by Django 4.2.7 on 2023-12-05 04:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0006_alter_order_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemorder',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
