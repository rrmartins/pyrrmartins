# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Artigo'
        db.create_table('blog_artigo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('conteudo', self.gf('django.db.models.fields.TextField')()),
            ('publicacao', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=100, blank=True)),
        ))
        db.send_create_signal('blog', ['Artigo'])


    def backwards(self, orm):
        
        # Deleting model 'Artigo'
        db.delete_table('blog_artigo')


    models = {
        'blog.artigo': {
            'Meta': {'ordering': "('-publicacao',)", 'object_name': 'Artigo'},
            'conteudo': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicacao': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']
