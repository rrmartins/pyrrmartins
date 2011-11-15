from django.db import models
from datetime import datetime

# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField( default=datetime.now, blank=True )

    class Meta:
        ordering = ('-publicacao',)

    def get_absolute_url(self):
        return '/artigo/%d/'%self.id
