# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssacount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]