# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 00:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20170721_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pc',
            name='fullData',
        ),
    ]
