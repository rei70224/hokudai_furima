# Generated by Django 2.1.5 on 2019-03-02 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_auto_20190119_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wanting_users',
            field=models.ManyToManyField(blank=True, related_name='wanting_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='watchlist',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='watchlist.WatchList'),
        ),
    ]