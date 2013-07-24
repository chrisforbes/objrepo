# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Record.metadata'
        db.alter_column(u'record_record', 'metadata', self.gf('jsonfield.fields.JSONField')())

    def backwards(self, orm):

        # Changing field 'Record.metadata'
        db.alter_column(u'record_record', 'metadata', self.gf('django.db.models.fields.TextField')())

    models = {
        u'record.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inherit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'link_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'out_links'", 'to': u"orm['record.Record']"}),
            'link_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_links'", 'to': u"orm['record.Record']"}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'record.record': {
            'Meta': {'object_name': 'Record'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['record.Record']", 'through': u"orm['record.Link']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['record']