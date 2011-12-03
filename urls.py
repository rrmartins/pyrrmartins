from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.models import Artigo
admin.autodiscover()
from blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index',
        {'queryset': Artigo.objects.all(),
         'date_field': 'publicacao'}),
    url(r'^admin/', include(admin.site.urls)),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict' : { 'ultimos': UltimosArtigos}}),
    (r'^artigo/(?P<slug>[\w_-]+)/$', 'blog.views.artigo'),
#    (r'^media/(.*)$', 'django.views.static.serve',
#        {'document_root': settings.MEDIA_ROOT}),
    (r'^contato/$', 'views.contato'),
    (r'^comments/', include('django.contrib.comments.urls')), 
    (r'^galeria/', include('galeria.urls')),
    (r'^tags/', include('tags.urls')),
)

if settings.LOCAL:
    urlpatterns += patterns('', (r'^media/(.*)$', 'django.views.static.serve',
                                  {'document_root': settings.MEDIA_ROOT}),
                   )
