# Generated by Django 3.2.23 on 2024-06-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0040_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$DaXNIYnalMR97P9NBfpSOi$70toYDF+IrXQx8dXSrSNyTkKCII6j79Doe7H3vPaTjg=', max_length=128, verbose_name='password'),
        ),
    ]
