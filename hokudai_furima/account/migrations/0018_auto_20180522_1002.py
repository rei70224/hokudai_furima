# Generated by Django 2.0.3 on 2018-05-22 01:02

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20180522_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=versatileimagefield.fields.VersatileImageField(blank=True, upload_to='media/public', verbose_name=''),
        ),
    ]
