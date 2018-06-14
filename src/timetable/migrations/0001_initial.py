# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[(0, 'понедельник'), (1, 'вторник'), (2, 'среда'), (3, 'четверг'), (4, 'пятница'), (5, 'суббота'), (6, 'воскресенье')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('start', models.TimeField(verbose_name='Начало')),
                ('finish', models.TimeField(verbose_name='Конец')),
                ('additional_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительная информация')),
                ('color', models.CharField(choices=[('#EF5350', 'красный'), ('#AB47BC', 'фиолетовый'), ('#7E57C2', 'глубоко фиолетовый'), ('#5C6BC0', 'индиго'), ('#42A5F5', 'голубой'), ('#29B6F6', 'легко-голубой'), ('#26C6DA', 'циан'), ('#66BB6A', 'бирюзовый'), ('#9CCC65', 'зеленый'), ('#D4E157', 'лайм'), ('#FFEE58', 'желтый'), ('#FFCA28', 'янтарный'), ('#FFA726', 'оранжевый'), ('#FF7043', 'глубоко оранжевый'), ('#8D6E63', 'желтый'), ('#8D6E63', 'коричневый'), ('#78909C', 'серый')], max_length=15, verbose_name='Цвет')),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Coach', verbose_name='Преподаватель')),
                ('day', models.ManyToManyField(to='timetable.Days', verbose_name='День')),
            ],
            options={
                'verbose_name_plural': 'Занятия',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('level', models.CharField(blank=True, max_length=255, null=True, verbose_name='Этаж')),
                ('number', models.CharField(max_length=255, verbose_name='Номер комнаты')),
            ],
            options={
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='timetable.Room', verbose_name='Комната')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('start', models.TimeField(verbose_name='Начало занятий')),
                ('end', models.TimeField(verbose_name='Конец занятий')),
                ('rest_days', models.ManyToManyField(related_name='rest_schedule', to='timetable.Days', verbose_name='Выходные дни')),
                ('work_days', models.ManyToManyField(related_name='work_schedule', to='timetable.Days', verbose_name='Рабочие дни')),
            ],
            options={
                'verbose_name_plural': 'Расписания',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Schedule', verbose_name='Расписание'),
        ),
    ]
