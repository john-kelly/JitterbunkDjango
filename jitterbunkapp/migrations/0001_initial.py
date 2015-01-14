# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bunk'
        db.create_table(u'jitterbunkapp_bunk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bunks_from_user', to=orm['jitterbunkapp.User'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bunks_to_user', to=orm['jitterbunkapp.User'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'jitterbunkapp', ['Bunk'])

        # Adding model 'User'
        db.create_table(u'jitterbunkapp_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'jitterbunkapp', ['User'])


    def backwards(self, orm):
        # Deleting model 'Bunk'
        db.delete_table(u'jitterbunkapp_bunk')

        # Deleting model 'User'
        db.delete_table(u'jitterbunkapp_user')


    models = {
        u'jitterbunkapp.bunk': {
            'Meta': {'object_name': 'Bunk'},
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bunks_from_user'", 'to': u"orm['jitterbunkapp.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bunks_to_user'", 'to': u"orm['jitterbunkapp.User']"})
        },
        u'jitterbunkapp.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['jitterbunkapp']