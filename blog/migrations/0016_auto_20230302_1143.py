# Generated by Django 2.2.11 on 2023-03-02 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_form_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='created',
        ),
        migrations.RemoveField(
            model_name='form',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='form',
            name='test',
        ),
        migrations.RemoveField(
            model_name='form',
            name='updated',
        ),
    ]
