# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-03 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180803_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='music.Artist'),
        ),
    ]
