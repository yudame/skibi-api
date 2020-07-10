# Generated by Django 3.0.7 on 2020-07-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20200622_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='backup_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='document',
            name='original_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='backup_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='original_url',
            field=models.URLField(default=''),
        ),
    ]