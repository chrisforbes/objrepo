"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from record.models import Record, Link

class RecordTests(TestCase):
    def setUp(self):
        self.q = Record.objects.create(
            title='Related object',
            metadata={
                'ex:another_property': 23,
            })
        self.r = Record.objects.create(
            title='A test record',
            metadata={
                'ex:llama_id': 42,
            })

    def test_metadata_one_record(self):
        d = self.r.all_metadata
        self.assertEqual(d['ex:llama_id'], 42)

    def test_metadata_noinherit(self):
        # this should work the same way.
        l = Link.objects.create(
            link_from=self.r,
            link_to=self.q,
            label='ex:related_to',
            inherit=False)

        d = self.r.all_metadata

        self.assertEqual(d['ex:llama_id'], 42)
        self.assertNotIn('ex:another_property', d)

    def test_metadata_inherit(self):
        # these records are linked, and marked to inherit prefixless.
        l = Link.objects.create(
            link_from=self.r,
            link_to=self.q,
            label='ex:related_to',
            inherit=True)

        d = self.r.all_metadata

        self.assertEqual(d['ex:llama_id'], 42)
        self.assertEqual(d['ex:another_property'], 23)
