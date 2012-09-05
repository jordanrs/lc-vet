# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.descripttion'
        db.add_column('calender_event', 'descripttion',
                      self.gf('django.db.models.fields.TextField')(default='desc'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.descripttion'
        db.delete_column('calender_event', 'descripttion')


    models = {
        'calender.event': {
            'Meta': {'object_name': 'Event'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'descripttion': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['calender']