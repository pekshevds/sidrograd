# Generated by Django 3.2.23 on 2024-01-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0019_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$mgfxdHusgZpYpsKsCRNNP3$248XxGqz0jdAvV3jM1WcfiAYcu88FtWL0yGpri7FE7Q=', max_length=128, verbose_name='password'),
        ),
    ]
