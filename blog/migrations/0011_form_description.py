# Generated by Django 2.2.11 on 2023-03-02 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_form_formfields'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
