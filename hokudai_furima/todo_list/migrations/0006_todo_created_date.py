# Generated by Django 2.0.3 on 2018-06-23 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0005_auto_20180602_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]