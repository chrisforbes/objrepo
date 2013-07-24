# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.inherit'
        db.add_column(u'record_link', 'inherit',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Link.prefix'
        db.add_column(u'record_link', 'prefix',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Link.inherit'
        db.delete_column(u'record_link', 'inherit')

        # Deleting field 'Link.prefix'
        db.delete_column(u'record_link', 'prefix')


    models = {
        u'record.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inherit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'link_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['record.Record']"}),
            'link_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['record.Record']"}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'record.record': {
            'Meta': {'object_name': 'Record'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['record.Record']", 'through': u"orm['record.Link']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['record']