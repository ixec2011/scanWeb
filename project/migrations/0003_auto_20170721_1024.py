# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_pc_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='limit',
            field=models.IntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
    ]
