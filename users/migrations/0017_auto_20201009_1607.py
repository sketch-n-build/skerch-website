# Generated by Django 3.1 on 2020-10-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_application'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name_plural': 'Applications'},
        ),
        migrations.AddField(
            model_name='application',
            name='about',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='application',
            name='q1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='q2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='q3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='q4',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='q5',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='q6',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='q7',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='q8',
            field=models.CharField(max_length=200),
        ),
    ]
