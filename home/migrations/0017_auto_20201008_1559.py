# Generated by Django 3.1 on 2020-10-08 14:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20201008_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_link',
            new_name='imagelink',
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='activity_time',
            field=models.DateField(default=datetime.datetime(2020, 10, 8, 14, 59, 38, 719324, tzinfo=utc)),
        ),
    ]
