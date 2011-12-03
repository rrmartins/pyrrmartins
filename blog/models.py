from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils.translation import ungettext
from django.utils.translation import ugettext as _


# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField( default=datetime.now, blank=True )
#    categoria = models.ManyToManyField('Categoria')
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    class Meta:
        ordering = ('-publicacao',)

    def __unicode__(self):
        return self.titulo

#    def get_absolute_url(self):
       # return '/artigo/%d/'%self.id
#       return reverse ('blog.views.artigo', kwargs={'slug': self.slug} )
    def get_absolute_url(self):
        return reverse( 'blog.views.artigo', kwargs={'slug': self.slug} )

		# SIGNALS
from django.db.models import signals
from utils.signals_comuns import slug_pre_save
signals.pre_save.connect(slug_pre_save, sender=Artigo)
# from django.template.defaultfilters import slugify
# def artigo_pre_save(signal, instance, sender, **kwargs):
#     """Este signal gera um slug automaticamente. Ele verifica se
# 	ja existe um artigo com o mesmo slug e acrescenta um numero ao
# 	final para evitar duplicidade"""
#     if not instance.slug:
#         slug = slugify(instance.titulo)
#         novo_slug = slug
#         contador = 0
#         while Artigo.objects.filter( slug=novo_slug ).exclude(id=instance.id).count() > 0:
#             contador += 1
#             novo_slug = '%s-%d'%(slug, contador)
#         instance.slug = novo_slug
# 	
# signals.pre_save.connect(artigo_pre_save, sender=Artigo)
