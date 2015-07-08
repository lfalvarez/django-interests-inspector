# -*- coding: utf-8 -*-
from django.db import models
from popolo.models import Person
from popolo.behaviors.models import Dateframeable
from autoslug import AutoSlugField


class Matter(models.Model):
    label = models.CharField(max_length=512)
    slug = AutoSlugField(populate_from='label')


class Interest(Dateframeable, models.Model):
    person = models.ForeignKey(Person)
    description = models.TextField(blank=True)
    matters = models.ManyToManyField(Matter, through='Conflict', related_name="interests")


class Conflict(models.Model):
    interest = models.ForeignKey(Interest)
    matter = models.ForeignKey(Matter)
    description = models.TextField(blank=True)
