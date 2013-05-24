# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Director'
        db.create_table('pelis_director', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('Cognom', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('Descripcio', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('Foto', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('pelis', ['Director'])

        # Adding model 'Genere'
        db.create_table('pelis_genere', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('NomGenere', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('pelis', ['Genere'])

        # Adding model 'Actor'
        db.create_table('pelis_actor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.TextField')(max_length=50, blank=True)),
            ('Cognom', self.gf('django.db.models.fields.TextField')(max_length=50, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('descripcio', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('Foto', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('pelis', ['Actor'])

        # Adding model 'Pelicula'
        db.create_table('pelis_pelicula', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Titol', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('Data', self.gf('django.db.models.fields.IntegerField')()),
            ('Argument', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('Director', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pelis.Director'])),
            ('Genere', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pelis.Genere'])),
            ('Foto', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('pelis', ['Pelicula'])

        # Adding M2M table for field Actor on 'Pelicula'
        m2m_table_name = db.shorten_name('pelis_pelicula_Actor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pelicula', models.ForeignKey(orm['pelis.pelicula'], null=False)),
            ('actor', models.ForeignKey(orm['pelis.actor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pelicula_id', 'actor_id'])


    def backwards(self, orm):
        # Deleting model 'Director'
        db.delete_table('pelis_director')

        # Deleting model 'Genere'
        db.delete_table('pelis_genere')

        # Deleting model 'Actor'
        db.delete_table('pelis_actor')

        # Deleting model 'Pelicula'
        db.delete_table('pelis_pelicula')

        # Removing M2M table for field Actor on 'Pelicula'
        db.delete_table(db.shorten_name('pelis_pelicula_Actor'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pelis.actor': {
            'Cognom': ('django.db.models.fields.TextField', [], {'max_length': '50', 'blank': 'True'}),
            'Foto': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Actor'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '50', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'descripcio': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pelis.director': {
            'Cognom': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'Descripcio': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'Foto': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Director'},
            'Nom': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pelis.genere': {
            'Meta': {'object_name': 'Genere'},
            'NomGenere': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pelis.pelicula': {
            'Actor': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pelis.Actor']", 'symmetrical': 'False'}),
            'Argument': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'Data': ('django.db.models.fields.IntegerField', [], {}),
            'Director': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pelis.Director']"}),
            'Foto': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'Genere': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pelis.Genere']"}),
            'Meta': {'object_name': 'Pelicula'},
            'Titol': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['pelis']