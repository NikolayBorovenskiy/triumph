# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 14:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20170109_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='title',
            new_name='name',
        ),
    ]
