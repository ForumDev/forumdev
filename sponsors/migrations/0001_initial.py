# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sponsor'
        db.create_table(u'sponsors_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.TextField')(default='')),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'sponsors', ['Sponsor'])


    def backwards(self, orm):
        # Deleting model 'Sponsor'
        db.delete_table(u'sponsors_sponsor')


    models = {
        u'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['sponsors']