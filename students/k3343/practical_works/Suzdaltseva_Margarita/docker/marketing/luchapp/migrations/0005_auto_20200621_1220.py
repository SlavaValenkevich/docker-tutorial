# Generated by Django 3.0.6 on 2020-06-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luchapp', '0004_auto_20200620_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='day_requested',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
