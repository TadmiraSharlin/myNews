# Generated by Django 3.0.2 on 2020-03-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200305_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='catid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='catname',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='news',
            name='show',
            field=models.IntegerField(default=0),
        ),
    ]
