# Generated by Django 3.2.23 on 2023-12-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0017_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$4IBxxW8tDScbyqtscD6Dhp$zdpqpyKc6BmeuJCw00NHUv3HJgRNgBOLHY/UAF4EWtc=', max_length=128, verbose_name='password'),
        ),
    ]
