# Generated by Django 3.2.23 on 2024-06-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0034_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$AKxgWDYLTmrTaxtxKJ6pLY$Fc+I/cH+aFuyu2hPmg4+acKSH/g7j/D1E0VNuzM9/AU=', max_length=128, verbose_name='password'),
        ),
    ]