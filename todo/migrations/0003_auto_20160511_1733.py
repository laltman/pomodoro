# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 21:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pomnumber',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
