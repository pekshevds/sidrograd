# Generated by Django 3.2.23 on 2024-01-31 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0025_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$kv93ZUIf1WZnrw7Sayvodx$XJOwz05x+6g+V727QXXerwhbFN7RqadjqBQI1/sdTqk=', max_length=128, verbose_name='password'),
        ),
    ]
