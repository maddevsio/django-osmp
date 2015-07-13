# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OSMP.txn_date'
        db.alter_column('osmp', 'txn_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'OSMP.txn_date'
        db.alter_column('osmp', 'txn_date', self.gf('django.db.models.fields.DateTimeField')(default=None))

    models = {
        u'osmp.osmp': {
            'Meta': {'object_name': 'OSMP', 'db_table': "'osmp'"},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'money': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'txn_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'txn_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['osmp']