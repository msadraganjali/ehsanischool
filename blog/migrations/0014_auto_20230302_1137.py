# Generated by Django 2.2.11 on 2023-03-02 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20230302_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='فرم زمان انتشار'),
        ),
    ]