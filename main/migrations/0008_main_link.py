# Generated by Django 3.0.2 on 2020-04-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200304_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
