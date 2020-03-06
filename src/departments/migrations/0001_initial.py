# Generated by Django 2.2.1 on 2020-03-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('short_name', models.CharField(max_length=3, unique=True, verbose_name='short name')),
                ('address', models.CharField(max_length=240, verbose_name='address')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated date')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ('-created',),
            },
        ),
    ]
