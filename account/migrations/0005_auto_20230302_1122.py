# Generated by Django 2.2.11 on 2023-03-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20230301_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(max_length=11, verbose_name='شماره مبایل'),
        ),
    ]
