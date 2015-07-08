#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-interests-inspector
------------

Tests for `django-interests-inspector` models module.
"""

from django.test import TestCase

from popolo.models import Person
from interests.models import Interest, Matter, Conflict


class InterestsTestCase(TestCase):
    fixtures = ['senadores', ]

    def setUp(self):
        pass

    def test_instanciate(self):
        '''Instanciate interests'''
        person = Person.objects.get(id='hernan-larrain-fernandez')
        interest = Interest.objects.create(person=person,
                                           description=u"Una descripción",
                                           start_date="1/1/1990",
                                           end_date='2/1/1990',)
        self.assertTrue(interest)
        self.assertEquals(interest.person, person)
        self.assertEquals(interest.description, u"Una descripción")
        self.assertEquals(interest.start_date, u"1/1/1990")
        self.assertEquals(interest.end_date, u"2/1/1990")


class MattersTestCase(TestCase):
    def setUp(self):
        pass

    def test_instanciate(self):
        matter = Matter.objects.create(label=u"AFP Estatal")
        self.assertTrue(matter)
        self.assertEquals(matter.label, u"AFP Estatal")
        self.assertTrue(matter.slug)
        self.assertEquals(matter.slug, u"afp-estatal")


class ConflictInterestTestCase(TestCase):
    fixtures = ['senadores', ]

    def setUp(self):
        pass

    def test_instanciate(self):
        person = Person.objects.get(id='hernan-larrain-fernandez')
        interest = Interest.objects.create(person=person,
                                           description=u"Una descripción",
                                           start_date="1/1/1990",
                                           end_date='2/1/1990',)
        matter = Matter.objects.create(label=u"AFP Estatal")
        conflict = Conflict.objects.create(interest=interest,
                                           matter=matter,
                                           description=u"This is why this is a conflict")

        self.assertTrue(conflict)
        self.assertEquals(conflict.interest, interest)
        self.assertEquals(conflict.matter, matter)
        self.assertTrue(conflict.description)
        self.assertIn(matter, interest.matters.all())
        self.assertIn(interest, matter.interests.all())
