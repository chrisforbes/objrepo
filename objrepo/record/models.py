from django.db import models
from jsonfield.fields import JSONField

class Record(models.Model):
    metadata = JSONField(blank=True)
    title = models.TextField()

    related = models.ManyToManyField('Record', through='Link')

class Link(models.Model):
    link_from = models.ForeignKey(Record, related_name='out_links')
    link_to = models.ForeignKey(Record, related_name='in_links')
    label = models.TextField()
    inherit = models.BooleanField()
    prefix = models.CharField(blank=True, null=True, max_length=128)
