# Generated by Django 2.0.6 on 2020-05-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_expert'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='info',
            field=models.TextField(default=' '),
        ),
    ]
