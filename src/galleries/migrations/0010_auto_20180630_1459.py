# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-30 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0009_auto_20180630_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEOGalleryTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser_title', models.CharField(default='Школа спортивного танца «Триумф»', max_length=200, null=True, verbose_name='Заголовок в браузере')),
                ('h1', models.CharField(default='Школа спортивного танца «Триумф»', max_length=200, null=True, verbose_name='Заголовок первого уровня')),
                ('key_words', models.TextField(default="школа танцев, клуб танцев, харьков, в харькове, харьковская, триумф, ирина балагула, контемн, детский танец, танцы для детей, бальные танцы, хип-хоп, политех, хпи, НТУ 'ХПИ'", null=True, verbose_name='Ключевые слова')),
                ('head_description', models.TextField(default='Школа спортивного танца «Триумф» — известная школа танцев в Харькове. Танцы для каждого. Широкое расписание. Профессиональные преподаватели. Удобное расположение в центре города. Звоните и присоеденяйтесь! (067)256-54-26. С танцем по жизни!', null=True, verbose_name='Описание для метатега')),
            ],
            options={
                'verbose_name_plural': 'SEO',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='browser_title',
            field=models.CharField(default='Школа спортивного танца «Триумф»', max_length=200, null=True, verbose_name='Заголовок в браузере'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='h1',
            field=models.CharField(default='Школа спортивного танца «Триумф»', max_length=200, null=True, verbose_name='Заголовок первого уровня'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='head_description',
            field=models.TextField(default='Школа спортивного танца «Триумф» — известная школа танцев в Харькове. Танцы для каждого. Широкое расписание. Профессиональные преподаватели. Удобное расположение в центре города. Звоните и присоеденяйтесь! (067)256-54-26. С танцем по жизни!', null=True, verbose_name='Описание для метатега'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='key_words',
            field=models.TextField(default="школа танцев, клуб танцев, харьков, в харькове, харьковская, триумф, ирина балагула, контемн, детский танец, танцы для детей, бальные танцы, хип-хоп, политех, хпи, НТУ 'ХПИ'", null=True, verbose_name='Ключевые слова'),
        ),
    ]
