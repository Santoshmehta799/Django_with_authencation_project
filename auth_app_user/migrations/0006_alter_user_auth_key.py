# Generated by Django 5.1 on 2024-08-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app_user', '0005_alter_user_auth_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_key',
            field=models.CharField(default='47a98aa51a07675f6069947f1978b911', max_length=32, unique=True),
        ),
    ]
