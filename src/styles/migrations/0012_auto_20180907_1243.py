# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-07 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0011_style_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['order'], 'verbose_name_plural': 'Танцевальные направления'},
        ),
        migrations.AlterField(
            model_name='style',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Порядковы номер'),
        ),
    ]
