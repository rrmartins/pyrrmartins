from django.contrib.syndication.feeds import Feed

from models import Artigo

class UltimosArtigos(Feed):
    title = 'Ultimos artigos do blog Rodrigo Martins'
    link = '/'

    def items(self):
        return Artigo.objects.all()

    def item_link(self, artigo):
        return '/artigo/%d/'%artigo.id


