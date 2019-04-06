# Generated by Django 2.1.5 on 2019-04-03 13:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import hokudai_furima.lecture.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LectureCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[hokudai_furima.lecture.models.has_no_singlequote], verbose_name='講義名')),
                ('description', models.TextField(max_length=2000, verbose_name='説明文')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lecture.LectureCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
