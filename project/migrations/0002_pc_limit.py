# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc',
            name='limit',
            field=models.IntegerField(null=True),
        ),
    ]
