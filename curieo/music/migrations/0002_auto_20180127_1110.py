# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='job_title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]