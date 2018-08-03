# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-03 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('marital_status', models.CharField(choices=[('married', 'married'), ('single', 'single'), ('other', 'other')], default='solteiro(a)', max_length=13)),
                ('name', models.CharField(max_length=32)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=9)),
                ('fullname', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('name', 'fullname'),
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='music.Album')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='music.Artist'),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([('album', 'order')]),
        ),
    ]