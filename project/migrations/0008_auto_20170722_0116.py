# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20170722_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]