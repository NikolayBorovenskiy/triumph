# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-14 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0007_auto_20170814_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='galleries.Gallery'),
        ),
    ]
