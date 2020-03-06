# Generated by Django 2.2.1 on 2020-03-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(blank=True, default='', max_length=60, verbose_name='model of a car'),
        ),
        migrations.AddField(
            model_name='car',
            name='passengers_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='maximum number of passengers allowed '),
        ),
        migrations.AddField(
            model_name='car',
            name='production_date',
            field=models.DateField(blank=True, null=True, verbose_name='date of production'),
        ),
        migrations.AddField(
            model_name='car',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='weight'),
        ),
    ]
