# Generated by Django 3.1 on 2020-10-08 21:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20201008_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='activity_time',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 21, 9, 11, 120730, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.BooleanField(default=False),
        ),
    ]
