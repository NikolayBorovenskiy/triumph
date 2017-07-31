# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20170212_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адресс')),
                ('phones', models.CharField(max_length=255, verbose_name='Телефоны')),
                ('work_time', models.CharField(max_length=255, verbose_name='Режим работы')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='school.School')),
            ],
            options={
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]