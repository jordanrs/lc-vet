# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClassRep'
        db.create_table('course_info_classrep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('school', self.gf('django.db.models.fields.IntegerField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('course_info', ['ClassRep'])


    def backwards(self, orm):
        # Deleting model 'ClassRep'
        db.delete_table('course_info_classrep')


    models = {
        'course_info.classrep': {
            'Meta': {'object_name': 'ClassRep'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.IntegerField', [], {})
        },
        'course_info.course': {
            'Meta': {'ordering': "['study_year', 'term']", 'object_name': 'Course'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'study_year': ('django.db.models.fields.IntegerField', [], {}),
            'term': ('django.db.models.fields.IntegerField', [], {})
        },
        'course_info.coursefile': {
            'Meta': {'object_name': 'CourseFile'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course_info.Course']"}),
            'course_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course_info.CourseSection']", 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        'course_info.coursesection': {
            'Meta': {'object_name': 'CourseSection'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course_info.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecturers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['course_info.Lecturer']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tips': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'course_info.infosetting': {
            'Meta': {'object_name': 'InfoSetting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'course_info.lecturer': {
            'Meta': {'ordering': "['surname']", 'object_name': 'Lecturer'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'teaching': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['course_info']