# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OSMP'
        db.create_table('osmp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('txn_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, db_index=True)),
            ('money', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('txn_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('account', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'osmp', ['OSMP'])


    def backwards(self, orm):
        # Deleting model 'OSMP'
        db.delete_table('osmp')


    models = {
        u'osmp.osmp': {
            'Meta': {'object_name': 'OSMP', 'db_table': "'osmp'"},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'txn_date': ('django.db.models.fields.DateTimeField', [], {}),
            'txn_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['osmp']