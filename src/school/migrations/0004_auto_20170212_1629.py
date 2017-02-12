# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 16:29
from __future__ import unicode_literals

import ckeditor.fields
import core.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanceHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Танцевальный зал',
            },
        ),
        migrations.CreateModel(
            name='DanceHallPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=core.utils.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('dance_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.DanceHall')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.AlterField(
            model_name='school',
            name='title',
            field=models.CharField(default='Труимф', max_length=60, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='dancehall',
            name='school',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
