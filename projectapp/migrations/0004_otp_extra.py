# Generated by Django 4.2.3 on 2023-07-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='extra',
            field=models.JSONField(default={}),
        ),
    ]
