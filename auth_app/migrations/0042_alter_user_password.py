# Generated by Django 3.2.23 on 2024-07-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0041_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$y1kmk8kdJr29z1ERJIZsP4$C17fxZfQbnZeTW7TScIvGq/xqbItJPgQBmC5EBisWXY=', max_length=128, verbose_name='password'),
        ),
    ]
