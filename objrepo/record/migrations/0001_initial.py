# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Record'
        db.create_table(u'record_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metadata', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'record', ['Record'])

        # Adding model 'Link'
        db.create_table(u'record_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['record.Record'])),
            ('link_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['record.Record'])),
            ('label', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'record', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Record'
        db.delete_table(u'record_record')

        # Deleting model 'Link'
        db.delete_table(u'record_link')


    models = {
        u'record.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'link_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['record.Record']"}),
            'link_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['record.Record']"})
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