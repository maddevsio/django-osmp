# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OSMP.method'
        db.add_column('osmp', 'method',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'OSMP.method'
        db.delete_column('osmp', 'method')


    models = {
        u'osmp.osmp': {
            'Meta': {'object_name': 'OSMP', 'db_table': "'osmp'"},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'money': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'txn_date': ('django.db.models.fields.DateTimeField', [], {}),
            'txn_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['osmp']