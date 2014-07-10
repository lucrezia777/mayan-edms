# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CreatorSingleton.lock_id'
        db.delete_column(u'acls_creatorsingleton', 'lock_id')


    def backwards(self, orm):
        # Adding field 'CreatorSingleton.lock_id'
        db.add_column(u'acls_creatorsingleton', 'lock_id',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=1, unique=True),
                      keep_default=False)


    models = {
        u'acls.accessentry': {
            'Meta': {'object_name': 'AccessEntry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_content_type'", 'to': u"orm['contenttypes.ContentType']"}),
            'holder_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'holder_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'access_holder'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['permissions.StoredPermission']"})
        },
        u'acls.creatorsingleton': {
            'Meta': {'object_name': 'CreatorSingleton'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'acls.defaultaccessentry': {
            'Meta': {'object_name': 'DefaultAccessEntry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'default_access_entry_class'", 'to': u"orm['contenttypes.ContentType']"}),
            'holder_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'holder_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'default_access_entry_holder'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['permissions.StoredPermission']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'permissions.storedpermission': {
            'Meta': {'ordering': "('namespace',)", 'unique_together': "(('namespace', 'name'),)", 'object_name': 'StoredPermission'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['acls']