# Generated by Django 2.0.3 on 2018-05-10 13:44

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20180510_0505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activate',
            old_name='key',
            new_name='token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='height',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ppoi',
        ),
        migrations.RemoveField(
            model_name='user',
            name='width',
        ),
        migrations.AddField(
            model_name='activate',
            name='uidb64',
            field=models.CharField(default='error', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=versatileimagefield.fields.VersatileImageField(blank=True, upload_to='img/account/', verbose_name=''),
        ),
    ]