# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lecturer'
        db.create_table('course_info_lecturer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.IntegerField')()),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('teaching', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('course_info', ['Lecturer'])

        # Adding model 'Course'
        db.create_table('course_info_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('school', self.gf('django.db.models.fields.IntegerField')()),
            ('study_year', self.gf('django.db.models.fields.IntegerField')()),
            ('term', self.gf('django.db.models.fields.IntegerField')()),
            ('difficulty', self.gf('django.db.models.fields.IntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('course_info', ['Course'])

        # Adding model 'CourseSection'
        db.create_table('course_info_coursesection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('tips', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course_info.Course'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('course_info', ['CourseSection'])

        # Adding M2M table for field lecturers on 'CourseSection'
        db.create_table('course_info_coursesection_lecturers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coursesection', models.ForeignKey(orm['course_info.coursesection'], null=False)),
            ('lecturer', models.ForeignKey(orm['course_info.lecturer'], null=False))
        ))
        db.create_unique('course_info_coursesection_lecturers', ['coursesection_id', 'lecturer_id'])

        # Adding model 'CourseFile'
        db.create_table('course_info_coursefile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('course_section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course_info.CourseSection'], blank=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course_info.Course'])),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('course_info', ['CourseFile'])

        # Adding model 'InfoSetting'
        db.create_table('course_info_infosetting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('course_info', ['InfoSetting'])


    def backwards(self, orm):
        # Deleting model 'Lecturer'
        db.delete_table('course_info_lecturer')

        # Deleting model 'Course'
        db.delete_table('course_info_course')

        # Deleting model 'CourseSection'
        db.delete_table('course_info_coursesection')

        # Removing M2M table for field lecturers on 'CourseSection'
        db.delete_table('course_info_coursesection_lecturers')

        # Deleting model 'CourseFile'
        db.delete_table('course_info_coursefile')

        # Deleting model 'InfoSetting'
        db.delete_table('course_info_infosetting')


    models = {
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