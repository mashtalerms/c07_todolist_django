# Generated by Django 4.1.2 on 2022-11-24 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_user_password_repeat"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="password_repeat",
        ),
    ]
