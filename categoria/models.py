from django.db import models
from django.utils.translation import ungettext
from django.utils.translation import ugettext as _

class Categoria(models.Model):
    descricao = models.CharField(max_length=40, unique=True)
   
    class Meta:
        ordering = ('descricao',)
