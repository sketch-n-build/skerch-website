# Generated by Django 3.1 on 2020-10-08 17:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20201008_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='activity_time',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 17, 12, 46, 946823, tzinfo=utc)),
        ),
    ]
