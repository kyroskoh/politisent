# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20170805_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.CharField(max_length=256, primary_key=True, serialize=False, unique=True),
        ),
    ]