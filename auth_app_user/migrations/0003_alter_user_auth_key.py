# Generated by Django 5.1 on 2024-08-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app_user', '0002_alter_user_auth_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_key',
            field=models.CharField(default='43934e82748baed33530d0f11ae36326', max_length=32, unique=True),
        ),
    ]
