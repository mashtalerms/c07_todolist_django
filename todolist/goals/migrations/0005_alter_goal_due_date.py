# Generated by Django 4.0.1 on 2022-12-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_alter_goal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='due_date',
            field=models.DateField(null=True, verbose_name='Дата выполнения'),
        ),
    ]
