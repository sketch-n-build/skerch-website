# Generated by Django 3.1 on 2020-10-13 15:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20201013_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='activity_time',
            field=models.DateField(default=datetime.datetime(2020, 10, 13, 15, 31, 31, 477109, tzinfo=utc)),
        ),
    ]
