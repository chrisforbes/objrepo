from django.db import models

class Record(models.Model):
    metadata = models.TextField(blank=True)
    title = models.TextField()

    related = models.ManyToManyField('Record', through='Link')

class Link(models.Model):
    link_from = models.ForeignKey(Record, related_name='+')
    link_to = models.ForeignKey(Record, related_name='+')
    label = models.TextField()
    pass
