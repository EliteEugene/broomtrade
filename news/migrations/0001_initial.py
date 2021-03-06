# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-22 18:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2016, 3, 22, 21, 36, 48, 335050), verbose_name='Опубликована')),
            ],
            options={
                'ordering': ['-posted'],
                'verbose_name_plural': 'новости',
                'verbose_name': 'новость',
            },
        ),
    ]
