# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssacount', '0004_ssacount_ping'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssacount',
            name='server_aes',
            field=models.CharField(default='', max_length=50),
        ),
    ]