# Generated by Django 4.2.7 on 2023-12-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0009_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$VSsG2HYUbtZvUqgT4MxMmB$Sq3lOxe5F5nxGx5DuwhFMbO9HDRTmz2VRNj5Clp09sQ=', max_length=128, verbose_name='password'),
        ),
    ]
