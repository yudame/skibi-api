# Generated by Django 3.0.7 on 2020-08-13 15:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_auto_20200812_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='unavailable_periods',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='breakfast_close_time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='breakfast_open_time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='brunch_close_time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='brunch_open_time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='dinner_close_time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='dinner_open_time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='lunch_close_time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='lunch_open_time',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='open hours', max_length=30)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('available_weekdays', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')]), blank=True, default=list, help_text='list of weekdays when schedule applies', size=None)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='shop.Menu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='limited_schedules',
            field=models.ManyToManyField(blank=True, to='shop.Schedule'),
        ),
    ]
