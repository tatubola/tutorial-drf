# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MARITAL_STATUS = (
    ('married', 'married'),
    ('single', 'single'),
    ('other', 'other'),
)

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
)


class Artist(models.Model):
    birthday = models.DateField()
    email = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )
    marital_status = models.CharField(
        choices=MARITAL_STATUS,
        default='solteiro(a)',
        max_length=13,
    )
    name = models.CharField(max_length=32)
    gender = models.CharField(
        choices=GENDER,
        default='female',
        max_length=9,
    )
    fullname = models.CharField(max_length=128)

    class Meta:
        ordering = ('name', 'fullname')
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return '[%s]' % (self.name)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    artist = models.ForeignKey(
        Artist,
        related_name='albums',
        on_delete=models.CASCADE
    )


class Track(models.Model):
    album = models.ForeignKey(
        Album,
        related_name='tracks',
        on_delete=models.CASCADE
    )
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)
