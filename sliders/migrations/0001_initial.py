# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.create_table(u'sliders_slider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=25)),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('descript', self.gf('django.db.models.fields.TextField')(default='')),
            ('short_name', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'sliders', ['Slider'])


    def backwards(self, orm):
        # Deleting model 'Slider'
        db.delete_table(u'sliders_slider')


    models = {
        u'sliders.slider': {
            'Meta': {'object_name': 'Slider'},
            'descript': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'short_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['sliders']