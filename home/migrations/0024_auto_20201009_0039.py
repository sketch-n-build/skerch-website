# Generated by Django 3.1 on 2020-10-08 23:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20201008_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='activity_time',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 23, 39, 53, 398556, tzinfo=utc)),
        ),
    ]
