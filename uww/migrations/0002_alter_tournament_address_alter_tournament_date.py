# Generated by Django 4.2 on 2023-06-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uww', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='date',
            field=models.CharField(max_length=20, verbose_name='Дата'),
        ),
    ]
