# Generated by Django 3.2.23 on 2024-10-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0054_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$dw1lIVqUrtcRtlWYcgcdbr$eAJ79HAzXnY3qiQQnU0xnadMK3/7oyXdNVhkdTDZO34=', max_length=128, verbose_name='password'),
        ),
    ]
