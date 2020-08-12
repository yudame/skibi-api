# Generated by Django 3.0.7 on 2020-08-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20200804_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='pushover_device_name',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AddField(
            model_name='shop',
            name='pushover_user_identifier',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]