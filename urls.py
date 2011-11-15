from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.models import Artigo
admin.autodiscover()
from blog.feeds import UltimosArtigos
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyblog.views.home', name='home'),
    # url(r'^pyblog/', include('pyblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.a]dmindocs.urls')),

    (r'^$', 'django.views.generic.date_based.archive_index',
        {'queryset': Artigo.objects.all(),
         'date_field': 'publicacao'}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict' : { 'ultimos': UltimosArtigos}}),
    (r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
 
)
